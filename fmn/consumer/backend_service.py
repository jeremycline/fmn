# -*- coding: utf-8 -*-
# Copyright (C) 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.

from __future__ import absolute_import

from collections import namedtuple
import logging
import json

from fedmsg_meta_fedora_infrastructure import fasshim
from pika import ConnectionParameters, exceptions as pika_exceptions
from pika.adapters import twisted_connection
from twisted.application import service
from twisted.internet import reactor, defer, protocol
import fedmsg
import fedmsg_meta_fedora_infrastructure

from . import fmn_fasshim, backends
from fmm.lib.models import Session, Filter


_log = logging.getLogger(__name__)
app_config = fedmsg.config.load_config()
fedmsg.meta_make_processors(**app_config)


# These monkey-patched shims cache results.
fmn_fasshim.make_fas_cache(**app_config)
fasshim.nick2fas = fmn_fasshim.nick2fas
fasshim.email2fas = fmn_fasshim.email2fas
fedmsg_meta_fedora_infrastructure.supybot.nick2fas = fmn_fasshim.nick2fas
fedmsg_meta_fedora_infrastructure.anitya.email2fas = fmn_fasshim.email2fas
fedmsg_meta_fedora_infrastructure.bz.email2fas = fmn_fasshim.email2fas
fedmsg_meta_fedora_infrastructure.mailman3.email2fas = fmn_fasshim.email2fas
fedmsg_meta_fedora_infrastructure.pagure.email2fas = fmn_fasshim.email2fas


# Create a few namedtuples to make the various tuples used throughout
# this module slightly clearer.
RabbitQueue = namedtuple(u'RabbitQueue', [u'queue', u'consumer_tag'])
SubscriptionEntry = namedtuple(u'SubscriptionEntry', [u'queue', u'requests'])


class BackendService(service.Service):
    """A Twisted service that sends notifications to end users."""

    name = 'FMN Backend Service'

    def __init__(self, config):

        self.running = False
        self.config = config

        self.backends = {
            'sse': backends.SSEBackend(config=self.config),
            'email': backends.EmailBackend(config=self.config),
            'irc': backends.IRCBackend(config=self.config),
            'android': backends.GCMBackend(config=self.config),
        }
        for key in self.backends.keys():
            if key not in self.config['fmn.backends']:
                del self.backends[key]

        self.expire_ms = int(app_config.get('fmn.sse.pika.msg_expiration', 3600000))
        self.amqp_host = self.app_config.get('fmn.pika.host', 'localhost')
        self.amqp_port = int(self.app_config.get('fmn.pika.port', 5672))
        self.amqp_parameters = ConnectionParameters(self.amqp_host, self.amqp_port)

        self.prefetch_count = app_config.get('fmn.sse.pika.prefetch_count',  5)
        self.connection = None

    @defer.inlineCallbacks
    def connect(self):
        """
        Construct and retrieve a queue from RabbitMQ.

        This will declare the queue in RabbitMQ if it doesn't already exist.

        The queue returned is a subclass of twisted.internet.defer.DeferredQueue.
        Calling ``get`` on the queue returns a ``Deferred`` that fires with
        (channel, method, properties, body) where the types are
        (pika.Channel, pika.spec.Basic.Deliver, pika.spec.BasicProperties, bytes).

        Afterwards you can do channel.basic_ack(delivery_tag=method.delivery_tag)
        to acknowledge message reciept.

        :param queue:           The queue to declare, bind to the exchange,
                                and consume from.
        :type  queue:           unicode str
        :param queue_arguments: custom arguments for the queue's construction
        :type  queue_agrements: dict

        :return: A Deferred that fires with a tuple of the queue to consume
                 messages from and a consumer tag.
        :rtype: Deferred of (pika.ClosableDeferredQueue, unicode str)
        """
        # TODO Handle errors appropriately
        cc = protocol.ClientCreator(
            reactor,
            twisted_connection.TwistedProtocolConnection,
            self.amqp_parameters,
        )
        tcp_connection = yield cc.connectTCP(self.amqp_host, self.amqp_port)
        self.connection = yield tcp_connection.ready
        channel = yield self.connection.channel()

        yield channel.queue_declare(queue='backends', durable=True, auto_delete=False)
        yield channel.basic_qos(prefetch_count=self.prefetch_count)
        deferred_queue, consumer_tag = yield channel.basic_consume(
            queue='backends',
            no_ack=False,
            exclusive=False,
        )
        queue = RabbitQueue(queue=deferred_queue, consumer_tag=consumer_tag)
        defer.returnValue(queue)

    @defer.inlineCallbacks
    def run(self):
        """
        The method that implements the FMN backend service.

        It connects to a RabbitMQ queue with messages that require delivery and
        dispatches them to backend implementations.
        """

        queue, consumer_tag = yield self.connect()

        while True:
            try:
                channel, method, properties, body = yield queue.queue.get()
            except pika_exceptions.ConsumerCancelled:
                # TODO better error handling
                _log.info('The server has canceled the AMQP consumer for '
                          'the "backends" queue')
                self.connect()
                continue

            try:
                body = json.loads(body)
            except ValueError:
                _log.exception('Unable to decode message "%s" to JSON', body)
                continue

            _log.info('Received message %s from the "backends" queue', body['raw_msg']['msg_id'])

            try:

                for recipient in body['recipients']:
                    # user_preference = self.preferences.get('{}_{}'.format(user, body['context']))
                    # TODO don't block
                    self.backend[body['context']].handle(
                        Session(), recipient, body['raw_msg']['body'])

                    if ('filter_oneshot' in recipient and recipient['filter_oneshot']):
                        idx = recipient['filter_id']
                        fltr = Filter.query.get(idx)
                        fltr.fired(Session())
                        _log.info('Marking one-shot filter as fired')

                yield channel.basic_ack(delivery_tag=method.delivery_tag)
            except:
                # TODO JSON errors, keyerrors, Errors from backend, SQLAlchemy errors, Pika
                # ack errors
                pass

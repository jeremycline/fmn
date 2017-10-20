================
FMN Architecture
================

This describes the various components of FMN and their architecture. FMN is split
into a web application front-end where users configure their message delivery
preferences and a number of back-end services that work together to collect
ZeroMQ messages via fedmsg, discover the list of users who should be notified,
and send those notifications.


System Diagram
==============

The general workflow is as follows::

                                                       +-------------+
                                                Read   |             |   Write
                                                +------+  prefs DB   +<------+
                                                |      |             |       |
     +                                          |      +-------------+       |
     |                                          |                            |   +------------------+   +--------+
     |                                          |                            |   |    |fmn.lib|     |   |        |
     |                                          v                            |   |    +-------+     |<--+  User  |
     |                                    +----------+                       +---+                  |   |        |
     |                                    |   fmn.lib|                           |  Central WebApp  |   +--------+
     |                                    |          |                           +------------------+
     |                             +----->|  Worker  +--------+
     |                             |      |          |        |
  fedmsg                           |      +----------+        |
     |                             |                          |
     |                             |      +----------+        |
     |   +------------------+      |      |   fmn.lib|        |       +--------------------+
     |   | fedmsg consumer  |      |      |          |        |       | Backend            |
     +-->|                  +------------>|  Worker  +--------------->|                    |
     |   |                  |      |      |          |        |       +-----+   +---+  +---+
     |   +------------------+      |      +----------+        |       |email|   |IRC|  |SSE|
     |                             |                          |       +--+--+---+-+-+--+-+-+
     |                             |      +----------+        |          |        |      |
     |                             |      |   fmn.lib|        |          |        |      |
     |                             |      |          |        |          |        |      |
     |                             +----->|  Worker  +--------+          |        |      |
     |                         RabbitMQ   |          |    RabbitMQ       |        |      |
     |                                    +----------+                   |        |      |
     |                                                                   v        v      v
     |
     |
     |
     v


The Back-end Services
=====================

The back-end is composed of a database that stores user preferences, a `fedmsg consumer`_
that subscribes to the ZeroMQ publisher sockets, one or more `celery workers`_, a
`celery beat`_ service that schedules periodic tasks (handled by the celery workers), and
a delivery service which is responsible for sending the actual notification. All these services
are tied together with the RabbitMQ AMQP message broker.


FedMsg Consumer
---------------

FMN provides a `fedmsg consumer`_ which can be run by the ``fedmsg-hub`` service. This service
subscribes to the ZeroMQ publishing sockets and dispatches `Celery`_ tasks to determine what
users are interested in notifications. These tasks are sent to `Celery workers`_ via RabbitMQ.


fmn-celerybeat
--------------

``fmn-celerybeat`` is a `Celery beat`_ service that dispatches periodic tasks that are handled
by the Celery workers.


fmn-worker
----------

``fmn-worker`` is a Celery worker service. You can run an arbitrary number of these workers on
multiple hosts. They need to be able to access RabbitMQ, Redis, and the database. Once it
determines who should receive notifications, it sends messages to the "backends" message queue.


fmn-backend
-----------

``fmn-backend`` is a Twisted application that handles the actual delivery of the notifications.
It subscribes to the "backends" AMQP message queue. You should only run one instance of this
service.


Database
--------

FMN uses `Alembic`_ to manage its database migrations. It is recommended that you use
PostgreSQL for your database. The database schema can be seen below:

.. figure:: images/database.png
   :align:  center

   Database schema.


.. _Alembic: http://alembic.zzzcomputing.com/en/latest/
.. _Celery: http://docs.celeryproject.org/en/latest/
.. _Celery beat: http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
.. _Celery workers: http://docs.celeryproject.org/en/latest/userguide/workers.html
.. _fedmsg consumer: https://fedmsg.readthedocs.io/en/stable/subscribing/

# -*- coding: utf-8 -*-
#
# <one line to give the library's name and a brief idea of what it does.>
# Copyright (C) <year>  <name of author>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""Tests for the :mod:`fmn.web.app` module."""

import unittest

from datanommer.models import Message

from fmn.lib import models
from fmn.web import app


def demo_match_func(config, message):
    return message['msg']['match']


class MatchExampleMessagesTests(unittest.TestCase):
    """Tests for the :func:`fmn.web.app._match_example_messages` function."""

    def setUp(self):
        self.user = models.User(
            openid=u'jcline.id.fedoraproject.org',
            openid_url=u'http://jcline.id.fedoraproject.org/',
        )
        self.context = models.Context(
            name=u'irc',
            description=u'irc backend',
            detail_name=u'irc nick',
            icon=u'user',
            placeholder=u'jcline',
        )
        self.preference = models.Preference(
            enabled=True,
            user=self.user,
            context=self.context,
        )
        self.filter = models.Filter(
            name='my filter',
            preference=self.preference
        )
        self.rule = models.Rule(
            filter=self.filter,
            code_path='fmn.tests.web.test_app:demo_match_func',
            _arguments='{}',
        )
        self.message = Message(topic='my.message.topic', _msg='{"match": false}')

    def test_no_matches(self):
        """Assert no results are returned if no messages match the filter."""
        results = app._match_example_messages(self.preference, self.filter, [self.message])

        self.assertEqual([], results)

    def test_matches(self):
        """Assert results are returned if messages match the filter."""
        self.message._msg = '{"match": true}'
        expected_results = [{
            'icon': None,
            'icon2': None,
            'link': '',
            'subtitle': '',
            'time': u'just now',
        }]
        results = app._match_example_messages(self.preference, self.filter, [self.message])

        self.assertEqual(expected_results, results)

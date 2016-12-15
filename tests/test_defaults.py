import unittest

import fmn.lib.models


class TestDefaults(unittest.TestCase):
    def setUp(self):
        self.sess = fmn.lib.models.init('sqlite://:memory:', debug=False, create=True)
        self.config = {'fmn.backends': ['irc', 'email', 'android']}
        self.valid_paths = fmn.lib.load_rules(root='fmn.rules')

        def mock_notify(self, openid, context, changed):
            if not hasattr(self, 'notified'):
                self.notified = []
            self.notified.append([openid, context, changed])

        self.original_notify = fmn.lib.models.FMNBase.notify
        fmn.lib.models.FMNBase.notify = mock_notify

    def tearDown(self):
        """ Remove the test.db database if there is one. """
        self.sess.rollback()
        fmn.lib.models.FMNBase.notify = self.original_notify

    def create_data(self):
        fmn.lib.models.Context.create(
            self.sess, name="email", description="the email",
            detail_name="email_address", icon="mail",
        )
        fmn.lib.models.User.get_or_create(
            self.sess,
            openid="ralph.id.fedoraproject.org",
            openid_url="http://ralph.id.fedoraproject.org/",
            create_defaults=True,
            detail_values=dict(email='shmalf@fedoraproject.org'),
        )
        fmn.lib.models.User.get_or_create(
            self.sess,
            openid="toshio.id.fedoraproject.org",
            openid_url="http://toshio.id.fedoraproject.org/",
            create_defaults=True,
        )

    def test_defaults_with_detail_value(self):
        self.create_data()
        preferences = fmn.lib.load_preferences(
            self.sess, self.config, self.valid_paths)
        pref = preferences[0]
        self.assertEqual(pref['user']['openid'], 'ralph.id.fedoraproject.org')
        self.assertEqual(pref['detail_values'], ['shmalf@fedoraproject.org'])
        self.assertEqual(pref['enabled'], True)

    def test_defaults_without_detail_value(self):
        self.create_data()
        preferences = fmn.lib.load_preferences(
            self.sess, self.config, self.valid_paths)
        pref = preferences[1]
        self.assertEqual(pref['user']['openid'], 'toshio.id.fedoraproject.org')
        self.assertEqual(pref['detail_values'], [])
        self.assertEqual(pref['enabled'], False)

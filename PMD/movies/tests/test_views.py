from django.core.urlresolvers import reverse
from test_plus.test import TestCase, settings


class TestHomeView(TestCase):

    def test_login_required(self):
        home_url = 'home'

        response = self.get(home_url)
        reversed_url = reverse(home_url)
        login_url = reverse(settings.LOGIN_URL)
        expected_url = "{0}?next={1}".format(login_url, reversed_url)
        self.assertRedirects(response, expected_url)

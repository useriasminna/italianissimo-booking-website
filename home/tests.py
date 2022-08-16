from django.test import TestCase


class TestViews(TestCase):
    """
    Unit Tests for Home App Views
    """

    def test_home_page(self):
        """ Test home page renders correct page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

"""
Contact App - Tests
----------------
Unit Tests for Contact App
"""
from django.test import TestCase


class TestViews(TestCase):
    """
    Unit Tests for Contact App Views
    """

    def test_contact_page(self):
        """ Test contact page renders correct page """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

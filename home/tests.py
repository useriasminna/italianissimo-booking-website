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
        
    def test_home_context(self):
        """ Test if Reviews, Meals, Favourites and Users are rendered to Create Home page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('review_list' in response.context)
        self.assertTrue('meals' in response.context)
        self.assertTrue('fav' in response.context)
        self.assertTrue('users' in response.context)


"""
Review App - Tests
----------------
Unit Tests for Review App.
"""
from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model


class TestViews(TestCase):
    """
    Unit Tests for Review App Views
    """

    def setUp(self):
        """ Create test login user"""

        # creates test user
        email = "testuser@yahoo.com"
        first = "test"
        last = "user"
        pswd = "T12345678."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)

    def test_review_page(self):
        """ Test if review page renders correct page """
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews.html')

    def test_review_context(self):
        """ Test if Review form, Reviews and Users are rendered
        to Create Reviews page"""
        response = self.client.get('/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('review_form' in response.context)
        self.assertTrue('reviews' in response.context)
        self.assertTrue('users' in response.context)

    def test_review_post(self):
        """ Test if The review was posted for the current user"""

        # creates a review post for testuser@yahoo.com
        new_review = {
            "rate": "5",
            "review_text": "Excellent"
        }

        self.client.get('/reviews/')
        self.client.post('/reviews/', new_review)

        # check if the review was registered to be posted by the current user
        response = self.client.get('/reviews/')
        reviews = response.context['reviews']
        self.assertEqual(reviews.count(), 1)
        self.assertTrue(reviews[0].author == self.user)

    def test_review_update(self):
        """ Test if The review of the current user is updating
        with the right values """
        # creates a review post for testuser@yahoo.com
        new_review = {
            "rate": "5",
            "review_text": "Excellent"
        }

        self.client.get('/reviews/')
        self.client.post('/reviews/', new_review)

        # create the values for the updated review
        updated_review = {
            "rate": "2",
            "review_text": "Not very satisfied"
        }

        response = self.client.get('/reviews/')
        reviews = response.context['reviews']

        now = datetime.now()
        # navigate to reviews and update the review
        self.client.get('/reviews/')
        self.client.post(
            '/reviews/review/' + str(
                reviews[0].pk) + '/update/', updated_review)

        # check if the review for the current user was updated with
        # the correct values
        response = self.client.get('/reviews/')
        reviews = response.context['reviews']
        self.assertEqual(reviews.count(), 1)
        self.assertTrue(reviews[0].author == self.user)
        self.assertTrue(reviews[0].rate == 2)
        self.assertTrue(reviews[0].review_text == "Not very satisfied")
        self.assertTrue((
            reviews[0].date_updated_on).strftime(
                "%Y-%m-%d %H:%M:%S") == now.strftime(
                    "%Y-%m-%d %H:%M:%S"))

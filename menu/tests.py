"""
Menu App - Tests
----------------
Unit Tests for Menu App.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Favourite, Meal


# Create your tests here.
class TestViews(TestCase):
    """
    Unit Tests for Menu App Views
    """

    def setUp(self):
        """ Create test login user and test meal object"""

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

        # creates test meal object
        self.meal = Meal.objects.create(
            name="Spaghetti Meatballs Bolognese",
            cover="image/upload/v1658868712/r6nmesvqug1mup664gwl.png",
            price="13",
            ingredients="spaghetti, beef mince, tomatoes, onion, garlic, eggs",
        )

    def test_menu_page(self):
        """ Test if menu page renders correct page """
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    def test_menu_context(self):
        """ Test if Meal list, Favourite form and Favourite list are rendered to Create Menu page"""
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('menu_list' in response.context)
        self.assertTrue('favourite_form' in response.context)
        self.assertTrue('favourites' in response.context)

    def test_favourite_meal_post(self):
        """Test if favourite meal is posted for current user"""

        # creates a favourite post for testuser@yahoo.com
        new_favourite = {
            "meal_id": "1",
        }

        self.client.get('/menu/')
        self.client.post('/menu/', new_favourite)

        response = self.client.get('/menu/')
        favourites = response.context['favourites']

        # check if the Favourites list contains the favourite post
        self.assertEqual(favourites.count(), 1)

        # check if the Favourites list contains the favourite post made for the current user
        self.assertTrue(favourites[0].user == self.user)

    def test_favourite_meal_delete(self):
        """ Test if Delete Favourite route from menu page deletes favourite"""

        # creates a favourite post for testuser@yahoo.com
        new_favourite = {
            "meal_id": "1",
        }

        self.client.get('/menu/')
        self.client.post('/menu/', new_favourite)

        response = self.client.get('/menu/')
        favourites = response.context['favourites']

        # check if the Favourites list contains the favourite post
        self.assertEqual(favourites.count(), 1)

        # navigate to menu and post to delete favourite url
        self.client.get('/menu/')
        self.client.post('/menu/favourite/' + str(favourites[0].pk) + '/remove/')

        # check if the Favourites list is empty after deletion
        response = self.client.get('/menu/')
        favourites = response.context['favourites']
        self.assertEqual(favourites.count(), 0)

    def test_favourite_meal_is_rendered_in_profile_page(self):
        """Test if the profile page renders only the favourite meals for the current user"""

        # creates a favourite post for testuser@yahoo.com
        new_favourite = {
            "meal_id": "1",
        }
        self.client.get('/menu/')
        self.client.post('/menu/', new_favourite)
        self.client.logout()

        # creates and log in user testuser2@yahoo.com
        email = "testuser2@yahoo.com"
        first = "test"
        last = "user2"
        pswd = "T12345679."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            email=email, first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)

        # creates a booking post for testuser2@yahoo.com
        new_favourite = {
            "meal_id": "1",
        }

        self.client.get('/menu/')
        self.client.post('/menu/', new_favourite)

        response = self.client.get('/bookings/profile/')
        meals = response.context['fav_meals']

        # check if the favorites list contains only one entry made from this account
        favourites = Favourite.objects.filter(user_id=self.user.email)
        self.assertEqual(favourites.count(), 1)

        # check if the meals list rendered in profile page contains only one meal because
        # only one favourite post has beend made from this account
        self.assertEqual(meals.count(), 1)

        # check if the meal rendered in profile page is posted to favourite by the current user
        self.assertTrue(favourites[0].user == self.user and favourites[0].meal == meals[0])

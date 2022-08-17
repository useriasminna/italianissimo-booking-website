import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime, date

from .forms import dateBookingForm
from .models import Table, User


class TestViews(TestCase):
    """
    Unit Tests for Booking App Views
    
    """

    def setUp(self):
            """ Create test login user and test table object"""
            
            #creates test user
            email = "testuser@yahoo.com"
            first = "test" 
            last = "user"
            pswd = "T12345678."
            user_model = get_user_model()
            self.user = user_model.objects.create_user(email=email,
                                                    first_name=first, last_name=last, password=pswd)
            logged_in = self.client.login(email=email, password=pswd)
            self.assertTrue(logged_in) 
            
            #creates test table object
            self.table = Table.objects.create(
            code = "A2",
            no_of_persons = "2",
            table_free_img = "image/upload/v1657289312/tw0rnaie5atrdrk6er1k.png",
            table_occupied_img = "image/upload/v1657289312/scgc1tjjysnphx8pdg6b.png",
        )
       
              
    def test_booking_page_redirects(self):
        """ Test if booking page redirects in case user is not logged in"""
        self.client.logout()
        response = self.client.get('/bookings/createbookings/')
        self.assertEqual(response.status_code, 302)

    def test_booking_page(self):
        """ Test if booking page renders correct page """
        response = self.client.get('/bookings/createbookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_booking_context(self):
        """ Test if Booking form, Tables and Bookings are rendered to Create Booking page"""
        response = self.client.get('/bookings/createbookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('booking_form' in response.context)
        self.assertTrue('tables_list' in response.context)
        self.assertTrue('bookings_list' in response.context)
        
    def test_profile_page_redirects(self):
        """ Test if profile page redirects in case user is not logged in"""
        self.client.logout()
        response = self.client.get('/bookings/profile/')
        self.assertEqual(response.status_code, 302)

    def test_profile_page(self):
        """ Test if profile page renders correct page """
        response = self.client.get('/bookings/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_profile_context(self):
        """ Test if Booking List and Favourite Meals are rendered to Create Profile page"""
        response = self.client.get('/bookings/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('fav_meals' in response.context)
        self.assertTrue('booking_list' in response.context)
          
    def test_created_booking_is_rendered_in_profile(self):
        """ Test if the profile page renders only the bookings made by the logged in user """
        
        #creates a booking post for testuser@yahoo.com
        new_booking = {
            "date" : "2022-08-25",
            "start_time" : "16:00:00",
            "end_time" : "19:00:00",
            "table_code" : "A2",
            "book_on_user" : "on",
        }
        
        self.client.get('/bookings/createbookings/')
        self.client.post('/bookings/createbookings/', new_booking)
        
        self.client.logout()
        
        #creates and log in user testuser2@yahoo.com
        email = "testuser2@yahoo.com"
        first = "test" 
        last = "user2"
        pswd = "T12345679."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(email=email,
                                                first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)
        
        #creates a booking post for testuser2@yahoo.com
        new_booking = {
            "date" : "2022-08-26",
            "start_time" : "16:00:00",
            "end_time" : "19:00:00",
            "table_code" : "A2",
            "book_on_user" : "on",
        }
        
        self.client.get('/bookings/createbookings/')
        self.client.post('/bookings/createbookings/', new_booking)
        
        #check if the booking_list response context rendered in profile page contains only 1 booking 
        response = self.client.get('/bookings/profile/')
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 1)
   
        #check if the booking_list response context rendered in profile page is made by testuser2@yahoo.com
        self.assertTrue(bookings[0].created_by == User.objects.get(email="testuser2@yahoo.com"))
        self.assertTrue(bookings[0].date == datetime.strptime("2022-08-26", "%Y-%m-%d").date())
        self.assertTrue(bookings[0].start_time == datetime.strptime("16:00:00", "%H:%M:%S").time())
        self.assertTrue(bookings[0].end_time == datetime.strptime("19:00:00", "%H:%M:%S").time())
        self.assertTrue(bookings[0].table == Table.objects.get(code="A2"))
        

    def test_profile_booking_delete(self):
            """ Test if Delete Booking route from profile page deletes booking"""
           
           #creates a booking post for testuser@yahoo.com
            new_booking = {
                "date" : "2022-08-25",
                "start_time" : "16:00:00",
                "end_time" : "19:00:00",
                "table_code" : "A2",
                "book_on_user" : "on",
            }
            
            self.client.get('/bookings/createbookings/')
            self.client.post('/bookings/createbookings/', new_booking)
            
            #check if the booking list contains the posted booking
            response = self.client.get('/bookings/profile/')
            bookings = response.context['booking_list']
            self.assertEqual(bookings.count(), 1)
            
            #navigate to profile and post to delete booking url
            self.client.get('/bookings/profile/')
            self.client.post('/bookings/profile/booking/' + str(bookings[0].pk) + '/remove/')
            
            #check if the booking list is empty after deletion
            response = self.client.get('/bookings/profile/')
            bookings = response.context['booking_list']
            self.assertEqual(bookings.count(), 0)
            
    def test_admin_manage_bookings_page_redirects(self):
        """ Test if admin manage bookings page redirects in case user is not logged in"""
        self.client.logout()
        response = self.client.get('/bookings/managebookings/')
        self.assertEqual(response.status_code, 302)
        
    def test_admin_manage_bookings_page_forbidden(self):
        """ Test if admin manage bookings page is forbidden in case user is not staff member"""
        response = self.client.get('/bookings/managebookings/')
        self.assertEqual(response.status_code, 403)

    def test_admin_manage_bookings_page(self):
        """ Test if admin manage bookings page renders correct page """
        self.user.staff = True
        self.user.save()
        response = self.client.get('/bookings/managebookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'managebookings.html')

    def test_admin_manage_bookings_context(self):
        """ Test if Date form, Date and Bookings are rendered to Create Admin Manage Booking page"""
        self.user.staff = True
        self.user.save()
        response = self.client.get('/bookings/managebookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('date_form' in response.context)
        self.assertTrue('date' in response.context)
        self.assertTrue('booking_list' in response.context)
        
    def test_admin_manage_bookings(self):
        """ Test if admin manage bookings page renders bookings from all user """
        
        #create and post booking for testuser@yahoo.com
        new_booking = {
                "date" : date.today(),
                "start_time" : "16:00:00",
                "end_time" : "19:00:00",
                "table_code" : "A2",
                "book_on_user" : "on",
            }
            
        self.client.get('/bookings/createbookings/')
        self.client.post('/bookings/createbookings/', new_booking)
        
        self.client.logout()
        
        #create and log in user testuser2@yahoo.com
        email = "testuser2@yahoo.com"
        first = "test" 
        last = "user2"
        pswd = "T12345679."
        user_model = get_user_model()
        self.user = user_model.objects.create_user(email=email,
                                                first_name=first, last_name=last, password=pswd)
        logged_in = self.client.login(email=email, password=pswd)
        self.assertTrue(logged_in)
        
        #create and post booking for testuser2@yahoo.com
        new_booking = {
                "date" : date.today(),
                "start_time" : "16:00:00",
                "end_time" : "19:00:00",
                "table_code" : "A2",
                "book_on_user" : "on",
            }
            
        self.client.get('/bookings/createbookings/')
        self.client.post('/bookings/createbookings/', new_booking)
        
        #made logged in user staff to be able to acces admin page
        self.user.staff = True
        self.user.save()
        
        #check if all the bookings are rendered in booking_list
        response = self.client.get('/bookings/managebookings/')
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 2)
        
    def test_admin_manage_bookings_filter(self):
        """ Test if admin manage bookings page renders bookings filtered by date """
        
        self.client.get('/bookings/createbookings/')
        
        #create and post first booking with today date
        new_booking = {
                "date" : date.today(),
                "start_time" : "16:00:00",
                "end_time" : "19:00:00",
                "table_code" : "A2",
                "book_on_user" : "on",
            }
                 
        self.client.post('/bookings/createbookings/', new_booking)
        
        #create and post second booking for 2022-08-10
        new_booking = {
                "date" : "2022-08-10",
                "start_time" : "16:00:00",
                "end_time" : "19:00:00",
                "table_code" : "A2",
                "book_on_user" : "on",
            }
            
        self.client.post('/bookings/createbookings/', new_booking)
        
        #made logged in user staff to be able to acces admin page
        self.user.staff = True
        self.user.save()
        
        #check if the default booking list contains only the bookings for today
        response = self.client.get('/bookings/managebookings/')
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 1)
        self.assertTrue(bookings[0].date == date.today())
        
        
        
        #add the value of 2022-08-10 as date for the form used to filter bookings 
        form_data = {
            "date" : datetime.strptime("2022-08-10", "%Y-%m-%d").date()
        }

        #check if the booking lists contains only the bookings filtered after the date submited in form
        response = self.client.get('/bookings/managebookings/', form_data)
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 1)
        self.assertTrue(bookings[0].date == datetime.strptime("2022-08-10", "%Y-%m-%d").date())
        
        
        
        #add a date value that doesn't exist in the booking database for the form used to filter bookings 
        form_data = {
            "date" : datetime.strptime("2022-05-01", "%Y-%m-%d").date()
        }

        #check if the booking lists is empty because there can't be found a booking for the provided date
        response = self.client.get('/bookings/managebookings/', form_data)
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 0)
        
    def test_admin_manage_bookings_delete(self):
        """ Test if Delete Booking route from admin manage bookings pages deletes booking"""
        
        #creates a booking post for testuser@yahoo.com
        new_booking = {
            "date" : date.today(),
            "start_time" : "16:00:00",
            "end_time" : "19:00:00",
            "table_code" : "A2",
            "book_on_user" : "on",
        }
        
        self.client.get('/bookings/createbookings/')
        self.client.post('/bookings/createbookings/', new_booking)
        
         #made logged in user staff to be able to acces admin page
        self.user.staff = True
        self.user.save()
        
        #check if the booking list contains the posted booking
        response = self.client.get('/bookings/managebookings/')
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 1)
         
        #navigate to profile and post to delete booking url
        self.client.get('/bookings/managebookings/')
        self.client.post('/bookings/managebookings/booking/' + str(bookings[0].pk) + '/remove/')
        
        #check if the booking list is empty after deletion
        response = self.client.get('/bookings/managebookings/')
        bookings = response.context['booking_list']
        self.assertEqual(bookings.count(), 0)
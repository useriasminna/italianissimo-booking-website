import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Booking, Table, User

class TestModels(TestCase):
    
    def create_booking(self, date="2022-08-23", start_time='14:00:00', end_time='15:00:00', table=Table.objects.get(code = "A1"),  customer_full_name="Iasmina Pal", customer_email="pal.iasmina@yahoo.com"  ):
        return Booking.objects.create(date=date, start_time=start_time, end_time=end_time, table=table, customer_full_name=customer_full_name,
                                      customer_email=customer_email, created_on=datetime.datetime.now(), created_by=User.objects.get(email = customer_email)) 

    def test_booking_creation(self):
        b = self.create_booking()
        self.assertTrue(isinstance(b, Booking))


class TestViews(TestCase):
    """
    Unit Tests for Booking App Views
    """

    def setUp(self):
            """ Create test login user """
            email = "testuser@yahoo.com"
            first = "test" 
            last = "user"
            pswd = "T12345678."
            user_model = get_user_model()
            self.user = user_model.objects.create_user(email=email,
                                                    first_name=first, last_name=last, password=pswd)
            logged_in = self.client.login(email=email, password=pswd)
            self.assertTrue(logged_in)
            
            
    def test_booking_page(self):
        """ Test booking page renders correct page """
        response = self.client.get('/bookings/createbookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

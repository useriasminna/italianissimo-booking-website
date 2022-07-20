import django_filters
from .models import *
from datetime import date

class BookingFilter(django_filters.FilterSet):
    
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time', 'table', 'customer_full_name', 'created_by']
    

"""
Booking App - Filters
----------------
Filters implementation for Booking App.
"""

import django_filters
from .models import Booking


class BookingFilter(django_filters.FilterSet):
    """Filter for bookings rendered in profile page"""
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time', 'table',
                  'customer_full_name', 'created_by']

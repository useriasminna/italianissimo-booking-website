"""
Booking App - Apps
----------------
App Configuration for Booking App.
"""

from django.apps import AppConfig


class BookingConfig(AppConfig):
    """Booking App configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

"""
Booking App - Admin
----------------
Admin Configuration for Booking App.
"""

from django.contrib import admin
from .models import Booking, Table

# Register your models here.
admin.site.register(Booking)
admin.site.register(Table)

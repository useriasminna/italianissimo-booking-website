"""
Review App - Admin
----------------
Admin Configuration for Review App.
"""
from django.contrib import admin
from review.models import Review


admin.site.register(Review)

"""
Contact App - URLS
----------------
URLS Configuration for Contact App
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Contact.as_view(), name='contact'),
]

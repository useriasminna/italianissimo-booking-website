"""
Users App - App
----------------
App Configuration for Users App.
"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users App Configuration"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

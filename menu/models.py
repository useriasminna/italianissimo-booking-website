"""
Menu App - Models
----------------
Models for Menu App.
"""
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class Meal(models.Model):
    """Model for Meal object"""
    name = models.CharField(max_length=100, unique=True)
    cover = CloudinaryField('image')
    price = models.FloatField()
    ingredients = models.CharField(max_length=1000)


class Favourite(models.Model):
    """Model for Favourite object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        to_field='email', blank=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True)

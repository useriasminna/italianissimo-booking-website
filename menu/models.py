from operator import truediv
from django.db import models
import json
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.forms import JSONField


# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100,unique=True)
    cover = CloudinaryField('image')
    price = models.FloatField()
    ingredients = models.CharField(max_length=1000)

class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email', blank=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, blank=True)
"""
Booking App - Models
----------------
Models for Booking App

"""
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class Table(models.Model):
    """Model for table object"""
    code = models.CharField(max_length=10, unique=True)
    table_free_img = CloudinaryField('free_image')
    table_occupied_img = CloudinaryField('occupied_image')
    no_of_persons = models.IntegerField(default=1)

    def __str__(self):
        return self.code


class Booking(models.Model):
    """Model for booking object"""
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE, to_field='code',
                              blank=True)
    customer_full_name = models.CharField(max_length=200,
                                          blank=True)
    customer_email = models.EmailField(max_length=200, blank=True)
    created_on = models.DateTimeField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   to_field='email',
                                   blank=True)

    class Meta:
        ordering = ['date', 'start_time']


class BookingQuery(models.Model):
    """Model for booking query form"""
    date = models.DateField()

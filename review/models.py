from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime

# Create your models here.

class Review(models.Model):
    rate = models.PositiveSmallIntegerField()
    review_text = models.TextField()
    now = datetime.datetime.now()
    date_created_on = models.DateTimeField(default=now.strftime("%Y-%m-%d %H:%M:%S"))
    date_updated_on = models.DateTimeField(default=now.strftime("%Y-%m-%d %H:%M:%S"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='email', blank=True)

    
    

    class Meta:
        ordering = ["date_updated_on"]

    def __str__(self):
        return f"Review {self.review_text} by {self.user}"
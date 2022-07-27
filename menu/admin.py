from django.contrib import admin

from menu.models import Favourite, Meal

# Register your models here.
admin.site.register(Meal)
admin.site.register(Favourite)
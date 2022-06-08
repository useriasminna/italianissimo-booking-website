from django.shortcuts import render
from django.views import View

# Create your views here.
class BaseTemplate(View):
    template_name = "base.html"

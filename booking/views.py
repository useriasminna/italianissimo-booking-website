from django.views.generic import TemplateView
from .forms import newBookingForm
from .models import Booking
from django.shortcuts import render
from django.views.generic.edit import FormView


# Create your views here.
class Booking(TemplateView):

    template_name = "booking.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super(Booking, self).get_context_data(*args,**kwargs)
        context['form'] = newBookingForm()
        return context
    
  
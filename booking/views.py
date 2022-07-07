from django.views.generic import TemplateView
from .forms import newBookingForm
from .models import Booking
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.
class Booking(TemplateView):

    template_name = "booking.html"
    
    def get_context_data(self,*args, **kwargs):
        context = super(Booking, self).get_context_data(*args,**kwargs)
        context['booking_form'] = newBookingForm()
        return context
    
    def post(self, request):
        
        if request.method=='POST':
            booking_form = newBookingForm(data=request.POST)
            booking_form.fields['book_on_user'].required = False
            if booking_form.is_valid():
                if ( booking_form.cleaned_data['book_on_user']):
                    
                    booking_form.instance.customer_email = request.user.email
                    
                    if (request.user.admin == "TRUE"):
                        booking_form.instance.customer_full_name = "admin"
                    else:
                        booking_form.instance.customer_full_name = request.user.first_name + " " + request.user.last_name
                    
                booking = booking_form.save(commit=False)
                booking.save()
                messages.success(request, 'Your booking was successfully registered')
                return HttpResponseRedirect('/bookings/createbookings') 
            
            else:
                return HttpResponse(booking_form.errors.as_json()) 
        else:
                booking_form = newBookingForm()            
    
        return render(request, 'booking.html', {'booking_form': booking_form,})
    
    

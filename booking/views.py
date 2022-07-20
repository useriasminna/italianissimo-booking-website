from datetime import date
from django.views.generic import TemplateView, ListView
from booking.filters import BookingFilter
from users.models import User
from .forms import newBookingForm
from .models import Table
from .models import Booking as BookingModel
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers import serialize
from django.db.models import Q
from datetime import date
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView

# Create your views here.
    
class Booking(LoginRequiredMixin, TemplateView):

    template_name = "booking.html"
    model = Table
    form_class = newBookingForm
    
    def get_context_data(self,*args, **kwargs):
        context = super(Booking, self).get_context_data(*args,**kwargs)
        context['booking_form'] = newBookingForm()      
        context['tables_list'] = serialize('json',Table.objects.all())
        context['bookings_list'] = serialize('json',BookingModel.objects.all())
        return context
    
    def post(self, request):
        
        if request.method=='POST':
            
            booking_form = newBookingForm(data=request.POST)
            booking_form.fields['book_on_user'].required = False 
             
            
            if booking_form.is_valid():
                booking_date = booking_form.cleaned_data['date']
                booking_start_time = booking_form.cleaned_data['start_time']
                booking_end_time = booking_form.cleaned_data['end_time']
                
                table_code = booking_form.cleaned_data['table_code']
                booking_table = Table.objects.get(code = table_code)
                
                user = User.objects.get(email = request.user.email)
                if ( booking_form.cleaned_data['book_on_user']):
                    
                    booking_customer_email = request.user.email
                    
                    
                    if (request.user.admin):
                        booking_customer_full_name = "Admin"
                    else:
                        booking_customer_full_name = request.user.first_name + " " + request.user.last_name
                else:
                    booking_customer_email = booking_form.cleaned_data['customer_email']
                    booking_customer_full_name = booking_form.cleaned_data['customer_full_name'] 
                    
                booking = BookingModel(date = booking_date, start_time = booking_start_time, end_time = booking_end_time,
                                       table = booking_table, customer_full_name = booking_customer_full_name,
                                       customer_email = booking_customer_email, created_by = user)
                booking.save()
                messages.success(request, 'Your booking was successfully registered')
                return HttpResponseRedirect('/bookings/createbookings') 
            
            else:
                messages.error(request, 'There was a problem submiting your booking. Please try again!')
                return HttpResponseRedirect('/bookings/createbookings')
                # return HttpResponse(booking_form.errors.as_json()) 
        else:
            booking_form = newBookingForm(request.GET)
        
        return render(request, 'booking.html', {'booking_form': booking_form,})
    

class BookingList(LoginRequiredMixin, FilterView):
    template_name = 'profile.html'
    paginate_by =  2
    filterset_class = BookingFilter
    list=BookingFilter()
    context_object_name ='booking_list'
    def get_queryset(self):
        today=date.today()
        return BookingModel.objects.filter(Q(created_by=self.request.user.email) & Q(date__gte=today) )

    
class BookingDeleteView(DeleteView, LoginRequiredMixin):
    model = BookingModel
    success_url = reverse_lazy('booking_list')
    template_name = 'profile.html'
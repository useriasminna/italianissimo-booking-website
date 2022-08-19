"""
Booking App - Views
----------------
Views for Booking App

"""
from datetime import date
import base64
import os
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.serializers import serialize
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django_filters.views import FilterView
from booking.filters import BookingFilter
from menu.models import Favourite, Meal
from users.models import User
from .models import Table
from .models import Booking as BookingModel
from .forms import NewBookingForm, DateBookingForm


class Booking(LoginRequiredMixin, TemplateView):
    """
    A view that provides a form to the user that creates a Booking entry
    """

    template_name = "booking.html"
    model = Table
    form_class = NewBookingForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['booking_form'] = NewBookingForm()
        context['tables_list'] = serialize('json', Table.objects.all())
        context['bookings_list'] = serialize('json', BookingModel.objects.all())
        return context

    def post(self, request):
        """Override post method"""

        if request.method == 'POST':

            booking_form = NewBookingForm(data=request.POST)
            booking_form.fields['book_on_user'].required = False

            if booking_form.is_valid():
                booking_date = booking_form.cleaned_data['date']
                booking_start_time = booking_form.cleaned_data['start_time']
                booking_end_time = booking_form.cleaned_data['end_time']
                table_code = booking_form.cleaned_data['table_code']
                booking_table = Table.objects.get(code=table_code)
                user = User.objects.get(email=request.user.email)

                if booking_form.cleaned_data['book_on_user']:
                    booking_customer_email = request.user.email

                    if request.user.admin:
                        booking_customer_full_name = "Admin"
                    else:
                        booking_customer_full_name = request.user.first_name +\
                                                     " " + request.user.last_name
                else:
                    booking_customer_email = booking_form.cleaned_data['customer_email']
                    booking_customer_full_name = booking_form.cleaned_data['customer_full_name']

                booking = BookingModel(date=booking_date, start_time=booking_start_time,
                                       end_time=booking_end_time, table=booking_table,
                                       customer_full_name=booking_customer_full_name,
                                       customer_email=booking_customer_email,
                                       created_on=datetime.datetime.now().
                                       strftime("%Y-%m-%d %H:%M:%S"),
                                       created_by=user,
                                       )
                booking.save()
                messages.success(request, 'Your booking was successfully registered')
                return HttpResponseRedirect('/bookings/createbookings')
            else:
                messages.error(request, 'There was a problem submiting your booking.'
                               ' Please try again!')
                return HttpResponseRedirect('/bookings/createbookings')
        else:
            booking_form = NewBookingForm(request.GET)

        return render(request, 'booking.html', {'booking_form': booking_form, })

    # def get(self, request, *args, **kwargs):
    #     booking_form = NewBookingForm(request.GET)
    #     return render(request, 'booking.html', {'booking_form': booking_form,})
    #     # return redirect('booking')


class BookingMealsList(LoginRequiredMixin, UserPassesTestMixin, FilterView):
    """
    A view that provides bookings and favourite meals data that coresponds to authenticated user
    """

    template_name = 'profile.html'
    paginate_by = 2
    filterset_class = BookingFilter
    context_object_name = 'booking_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        favourites = Favourite.objects.filter(user_id=self.request.user.email).values_list('meal')
        context['fav_meals'] = Meal.objects.filter(pk__in=favourites)
        return context

    def get_queryset(self):
        today = date.today()
        return BookingModel.objects.filter(Q(created_by=self.request.user.email) &\
                                           Q(date__gte=today))

    def test_func(self):
        return not self.request.user.is_staff


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that deletes a booking entry from the database.
    The action is performed only if the authenticated user is the author of the booking.
    """

    model = BookingModel
    success_url = reverse_lazy('booking_list')
    template_name = 'profile.html'

    def test_func(self):
        item = self.get_object()
        return self.request.user == item.created_by


class BookingListAdmin(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    A view that provides the list of bookings to be accesed only by a staff member.
    The view also provides a form to filter the bookings by date.
    """

    model = BookingModel
    template_name = 'managebookings.html'

    def get(self, request):
        if request.method == 'GET':
            today = date.today()
            date_form = DateBookingForm(data=request.GET)
            if date_form.is_valid():
                bdate = date_form.cleaned_data['date']
                if bdate:
                    query = BookingModel.objects.filter(date=bdate)
                else:
                    bdate = today
                    query = BookingModel.objects.filter(date=bdate)
                context = {'date_form': date_form,
                           'date': bdate,
                           'booking_list': query}

        return render(request, 'managebookings.html', context)

    def test_func(self):
        return self.request.user.is_staff


class BookingDeleteViewAdmin(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view that deletes a booking entry from the database.
    The action is performed only if the authenticated user is a staff member.
    """

    model = BookingModel
    template_name = 'managebookings.html'

    def get_success_url(self):
        bdate = self.get_object().date
        csrf = base64.b64encode(os.urandom(64))
        return '/bookings/managebookings/?csrfmiddlewaretoken=' + csrf.decode("utf-8") +\
               '&date=' + bdate.strftime("%Y-%m-%d")

    def test_func(self):
        return self.request.user.is_staff

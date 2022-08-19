"""
Booking App - Forms
----------------
Forms for Booking App

"""

from datetime import date
from django import forms
from .models import Booking, BookingQuery


class NewBookingForm(forms.ModelForm):
    """
    Form for the Booking Model
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datePicker', 'class': 'form-control',
                                                         'type': 'date', 'name': 'datePicker'}))
    start_time = forms.TimeField(widget=forms.TimeInput(
                 attrs={'id': 'startTime', 'class': 'form-control', 'type': 'time',
                        'name': 'startTime', 'step': '3600'}))
    end_time = forms.TimeField(widget=forms.TimeInput(
               attrs={'id': 'endTime', 'class': 'form-control',
                      'type': 'time', 'name': 'endTime', 'step': '3600'}))
    customer_full_name = forms.CharField(widget=forms.TextInput(
                         attrs={'id': 'fullName', 'class': 'form-control',
                                'type': 'text', 'name': 'fullName'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(
                     attrs={'id': 'email', 'class': 'form-control',
                            'type': 'email', 'name': 'email'}))
    book_on_user = forms.BooleanField(widget=forms.CheckboxInput(
                   attrs={'id': 'bookAuthenticate', 'type': 'checkbox',
                          'name': 'bookAuthenticate'}))
    table_code = forms.ChoiceField(widget=forms.Select(
                 attrs={'id': 'tableCode', 'class': 'form-select',
                        'type': 'select', 'name': 'tableCode'}),
                 choices=(("A1", "A1"), ("A2", "A2"), ("A3", "A3"), ("B1", "B1"),
                          ("B2", "B2"), ("B3", "B3"), ("C1", "C1"), ("C2", "C2"), ("C3", "C3")))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['book_on_user'].required = False
        self.fields['customer_full_name'].required = True
        self.fields['customer_email'].required = True

    def clean(self):
        user_book = self.cleaned_data.get('book_on_user', False)
        if user_book:
            name = self.cleaned_data.get('customer_full_name', False)
            email = self.cleaned_data.get('customer_email', False)
            if name is False:
                del self.errors['customer_full_name']
            if email is False:
                del self.errors['customer_email']

        return self.cleaned_data

    class Meta:
        model = Booking
        fields = "__all__"


class DateBookingForm(forms.ModelForm):
    """
    Form for the BookingQuery Model
    It is used for filtering the bookings in admin manage booking page
    """
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'datePicker',
                                                         'class': 'form-control',
                                                         'type': 'date', 'name': 'datePicker',
                                                         'value': date.today()}),
                           initial=date.today())

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['date'].required = False
        self.fields['date'].label = "Filter By Date:"
        self.fields['date'].initial = date.today()

    class Meta:
        """Meta class"""
        model = BookingQuery
        fields = ['date']

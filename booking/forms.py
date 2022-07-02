from django import forms
from .models import Booking

class newBookingForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'id':'datePicker', 'class':'form-control', 'type':'date', 'name':'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'id':'startTime', 'class':'form-control', 'type':'time', 'name':'startTime', 'step':'3600'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'id':'endTime', 'class':'form-control', 'type':'time', 'name':'endTime', 'step':'3600'}))
    customer_full_name = forms(widget=forms.TextInput(attrs={'id':'fullName', 'class':'form-control', 'type':'text', 'name':'fullName'}))
    customer_email = forms(widget=forms.EmailInput(attrs={'id':'email', 'class':'form-control', 'type':'email', 'name':'email'}))
    book_user = forms(widget=forms.CheckboxInput(attrs={'id':'bookAuthenticate', 'type':'checkbox', 'name':'bookAuthenticate'}))

class Meta:
    # specify model to be used
    model = Booking
    exclude = ()
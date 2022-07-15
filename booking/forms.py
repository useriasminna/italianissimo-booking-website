from operator import ne
from random import choices
from django import forms
from .models import Booking

class newBookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'id':'datePicker', 'class':'form-control', 'type':'date', 'name':'datePicker'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'id':'startTime', 'class':'form-control', 'type':'time', 'name':'startTime', 'step':'3600'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'id':'endTime', 'class':'form-control', 'type':'time', 'name':'endTime', 'step':'3600'}))
    customer_full_name = forms.CharField (widget=forms.TextInput(attrs={'id':'fullName', 'class':'form-control', 'type':'text', 'name':'fullName'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'email', 'class':'form-control', 'type':'email', 'name':'email'}))
    book_on_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={'id':'bookAuthenticate', 'type':'checkbox', 'name':'bookAuthenticate'}))
    table_code = forms.ChoiceField (widget=forms.Select(attrs={'id':'tableCode', 'class':'form-select', 'type':'select', 'name':'tableCode'}),
                                    choices=(("A1","A1"), ("A2","A2"), ("A3","A3"),("B1","B1"), ("B2","B2"), ("B3","B3"),("C1","C1"), ("C2","C2"), ("C3","C3")) )    
    
    def __init__(self, *args, **kwargs):
        
        super(newBookingForm, self).__init__(*args, **kwargs)

        self.fields['book_on_user'].required = False
        self.fields['customer_full_name'].required = True
        self.fields['customer_email'].required = True

    def clean(self):
        user_book = self.cleaned_data.get('book_on_user', False)
        # make contact inputs not required when book_on_user is checked
        if user_book:
            del self.errors['customer_full_name']
            del self.errors['customer_email']
        return self.cleaned_data
    
    class Meta:
        # specify model to be used
        model = Booking
        fields = "__all__"
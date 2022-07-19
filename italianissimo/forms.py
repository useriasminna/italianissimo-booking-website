from allauth.account.forms import SignupForm
from django import forms
 
 
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
 
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        if any(not c.isalnum() for c in first_name):
            raise forms.ValidationError("No special characters allowed")
        elif any(c.isdigit() for c in first_name):
            raise forms.ValidationError("No numbers allowed")
        return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if any(not c.isalnum() for c in last_name):
            raise forms.ValidationError("No special characters allowed")
        elif any(c.isdigit() for c in last_name):
            raise forms.ValidationError("No numbers allowed")
        return last_name
       
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user
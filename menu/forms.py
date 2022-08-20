"""
Menu App - Forms
----------------
Forms for Menu App.
"""
from django import forms
from menu.models import Favourite


class SetFavourite(forms.ModelForm):
    """Form for setting meal state of favourite"""
    meal_id = forms.CharField (widget=forms.TextInput(attrs={'class':'mealId', 'type':'hidden'}) )
    class Meta:
        model = Favourite
        fields = []

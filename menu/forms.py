from django import forms
from menu.models import Favourite



class addFavourite(forms.ModelForm):
    meal_id = forms.CharField (widget=forms.TextInput(attrs={'class':'mealId', 'type':'hidden'}) )
    class Meta:
        model = Favourite
        fields = []
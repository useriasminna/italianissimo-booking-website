"""
Review App - Forms
----------------
Forms for Review App.
"""
from django import forms
from review.models import Review


class ReviewForm(forms.ModelForm):
    """Form for add/update review"""
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'rateValue', 'type': 'hidden'}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'addReviewText', 'class': 'form-control',
        'rows': '6', 'cols': '100'}), label="Add a message:")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].required = False

    class Meta:
        model = Review
        fields = ['review_text', 'rate']

class UpdateReviewForm(forms.ModelForm):
    """Form for add/update review"""
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'id': 'updateRateValue',
                                                              'type': 'hidden'}))
    review_text = forms.CharField(widget=forms.Textarea(attrs={
        'id': 'updateReviewText', 'class': 'form-control',
        'rows': '6', 'cols': '100'}), label="Update your message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rate'].required = False

    class Meta:
        model = Review
        fields = ['review_text', 'rate']

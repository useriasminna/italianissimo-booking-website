from django import forms

from review.models import Review


class newReviewForm(forms.ModelForm):
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'id':'rateValue','type':'hidden'}))
    review_text = forms.CharField (widget=forms.Textarea(attrs={'id':'reviewText', 'class':'form-control', 'type':'text', 'name':'reviewText', 'rows':'6'}), label="") 
    
 
    def __init__(self, *args, **kwargs): 
        super(newReviewForm, self).__init__(*args, **kwargs)
        self.fields['rate'].required = False
    
    
    class Meta:
        model = Review
        fields = ['review_text', 'rate']
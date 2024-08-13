from django import forms
from .models import Post,Review
    



class postForm(forms.ModelForm):
    class Meta:
        model=Post
        #fields='__all__'
        exclude =['user',]

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        #fields='__all__'
        exclude=['user','post','publish_date']

    
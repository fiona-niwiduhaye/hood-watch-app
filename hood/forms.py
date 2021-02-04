from django import forms
from .models import  Profile
from .models import  NeighbourHood
from .models import Posts
from .models import Businesses
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['profile','pub_date', 'poster_id']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'userId']


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Businesses
        exclude = ['user']
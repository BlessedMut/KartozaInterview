from django import forms

from .models import Profiles


# User creation form
class UserForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('username', 'first_name', 'email', 'password', 'address', 'lon', 'lat', 'phone')

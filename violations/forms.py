from django import forms
from violations.models import RoadViolation
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

class SignInForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField(widget=forms.PasswordInput())

class RoadViolationForm(forms.ModelForm):
    class Meta:
        model = RoadViolation
        fields = ['description', 'vehicle_image']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserProfile


class Registration(UserCreationForm):
    class Meta():
        model = UserProfile
        fields = ('email',)

    def clean_email(self):
        email=self.cleaned_data.get('email')
        print(email)
        if User.objects.filter(email=email).count()>0:
            raise forms.ValidationError("Already Exist")
        return email


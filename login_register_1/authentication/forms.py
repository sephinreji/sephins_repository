from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registration(UserCreationForm):
    class Meta():
        model = User
        fields = ['username',  'password1', 'password2','email']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        print(email)
        if User.objects.filter(email=email).count()>0:
            raise forms.ValidationError("Already Exist")
        return email


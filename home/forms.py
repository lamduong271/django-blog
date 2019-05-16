from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data: #check if password1 is filled yet? in cleaned_data
            password1 = self.cleaned_data['password1'] # get password1 from cleaned_data
            password2 = self.cleaned_data['password2']
            if(password1==password2 and password1): # contain password 1 spaces is OK
                return password2
            raise forms.ValidationError("Not valid password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Not allow special characters ")
        try: User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("username already exists")

    def save(sefl):
        User.objects.create_user(username=sefl.cleaned_data['username'],email=sefl.cleaned_data['email'],password=sefl.cleaned_data['password1'])




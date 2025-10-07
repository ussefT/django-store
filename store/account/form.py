from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from phonenumber_field.phonenumber import PhoneNumber

class SignupForm(forms.Form):
    name=forms.CharField(label='name',max_length=100)
    family=forms.CharField(label='family',max_length=100)
    email=forms.EmailField()
    password1=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
    password2=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
    phone=forms.CharField(label='phone',max_length=100,validators=[validators.RegexValidator(r'(\+98|09|9)?9\d{8}$')
                                                                   ,validators.MinLengthValidator(5),
                                                                   validators.MaxLengthValidator(20)])
    # phone=PhoneNumber()

    # if validatore for form is not exist this a way
    def clean_name(self):
        if self.cleaned_data['name']==self.cleaned_data['password1']:
            raise ValidationError('Name is not same password')
        return self.cleaned_data['name']
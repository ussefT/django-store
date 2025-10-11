from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from phonenumber_field.phonenumber import PhoneNumber
from .  import models


# class SignupForm(forms.Form):
#     name=forms.CharField(label='name',max_length=100)
#     family=forms.CharField(label='family',max_length=100)
#     email=forms.EmailField()
#     password1=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
#     password2=forms.CharField(label='password',max_length=100,widget=forms.PasswordInput())
#     phone=forms.CharField(label='phone',max_length=100,validators=[validators.RegexValidator(r'(\+98|09|9)?9\d{8}$')
#                                                                    ,validators.MinLengthValidator(5),
#                                                                    validators.MaxLengthValidator(20)])
#     # phone=PhoneNumber()
#
#     # if validatore for form is not exist this a way
#     def clean_name(self):
#         if self.data['name']==self.data['password1']:
#             raise ValidationError('Name is not same password')
#         return self.data['name']

## use default form django
# class SignupFomr(forms.ModelForm):
#     class Meta:
#         model=models.User
#         fields=['first_name','last_name','email','phone']
#         # fields="__all__" # show all fields
#         exclude=['is_superuser','is_staff','is_active'] # not active


from django.contrib.auth.forms import UserCreationForm

# use model default django user auth
class SignUpForm(UserCreationForm):
    class Meta:
        model=models.User
        exclude=['is_superuser','user_permissions'
            ,'last_login','date_joined','avatar','password'
                 'groups','is_staff','is_active'] # not active

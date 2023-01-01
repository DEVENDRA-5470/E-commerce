from django import forms
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation 
from .models import Customer

# # CREATING USER USING FORM API AND BUILT IN USER AUTH FORMS:


# class my_user_registration(UserCreationForm):
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password","placeholder":"Password"}),
        
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password","placeholder":"Re-Password"}),
#         strip=False,
      
#     )


#     class Meta:
#         model=User
#         fields=['username','email','password1','password2']
#         labels={"email":"Email",'username':'Username'}
#         widgets={'username':forms.TextInput(attrs={"placeholder":"Enter Username"}),
#                  'email':forms.EmailInput(attrs={"placeholder":"Email address"}),
#         }


class User_login(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,"placeholder":"Enter user name"}))
    password = forms.CharField(
        label=_("Password Confirm:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password","placeholder":"Confirm Password"}),)


class Password_change(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={"placeholder":"Enter your old password"}))

    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.TextInput(attrs={"placeholder":"Enter your New password"}),help_text=password_validation.password_validators_help_text_html())

    new_password2=forms.CharField(label=_("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs={"placeholder":"Re-password"}))


class Customer_Profile(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','mob','city','state','zipcode']
        label={"mob":"Mobile"}
        widgets={
            'name':forms.TextInput(),
            'mob':forms.NumberInput(),
            'city':forms.TextInput(),
            'state':forms.Select(),
            'zipcode':forms.NumberInput(),
        }


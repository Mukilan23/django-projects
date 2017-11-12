from django import forms
from appTwo.models import User
from django.core import validators

def check_for_capital(value):
    if (value[0]).isupper():
     pass
    else :
      raise forms.ValidationError("Sorry! your username must start with a capital letter ")

class NewUserForm(forms.ModelForm):
    Username=forms.CharField(validators=[check_for_capital])

    class Meta:
            model = User
            fields='__all__'

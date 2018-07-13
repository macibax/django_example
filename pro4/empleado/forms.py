
from django import forms
from django.core import validators
from django.forms import ModelForm
from empleado.models import Empleado, Puesto, UserProfileInfo

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class RegEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class RegPuesto(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = "__all__"

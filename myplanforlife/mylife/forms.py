from django import forms
from .models import MyPlan
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyPlanForm(forms.ModelForm):
    class Meta:
        model = MyPlan
        fields = '__all__' 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

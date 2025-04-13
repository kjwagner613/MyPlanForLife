from django import forms
from .models import MyPlan
from .models import MealPlan
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyPlanForm(forms.ModelForm):
    class Meta:
        model = MyPlan
        fields = '__all__' 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': datetime.date.today().isoformat()}),
        }

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['meal', 'date', 'time_of_day']
        widgets = {
           'date': forms.DateInput(attrs={'type': 'date', 'value': datetime.date.today().isoformat()}),
        }

        
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

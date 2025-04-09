from django.shortcuts import render
from pyexpat.errors import messages
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MyPlan, Meal
from .forms import MyPlanForm
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
# Create your views here.

def custom_logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

class HomeView(TemplateView):
    template_name = 'home.html'

class LogoutView(TemplateView):
    template_name = 'registration/logged_out.html'

class MyPlanListView(ListView):
    model = MyPlan
    template_name = 'mylife/myplan_list.html'
    context_object_name = 'myplans'

class MyPlanDetailView(DetailView):
    model = MyPlan
    template_name = 'mylife/myplan_detail.html'

class MyPlanCreateView(LoginRequiredMixin, CreateView):
    model = MyPlan
    form_class = MyPlanForm
    template_name = 'mylife/myplan_form.html'
    success_url = reverse_lazy('myplan_list')

class MyPlanUpdateView(UpdateView):
    model = MyPlan
    form_class = MyPlanForm
    template_name = 'mylife/myplan_form.html'
    success_url = reverse_lazy('myplan_list')

class MyPlanDeleteView(DeleteView):
    model = MyPlan
    template_name = 'mylife/myplan_confirm_delete.html'
    success_url = reverse_lazy('myplan_list')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class MealListView(ListView):
    model = Meal
    template_name = 'mylife/meal_list.html'
    context_object_name = 'meals'

class MealCreateView(CreateView):
    model = Meal
    fields = ['name', 'mealtime']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')


class MealUpdateView(UpdateView):
    model = Meal
    meals = ['name']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealDeleteView(DeleteView):
    model = Meal
    template_name = 'mylife/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')
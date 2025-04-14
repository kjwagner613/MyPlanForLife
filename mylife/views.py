from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MyPlan, Meal

from .forms import MyPlanForm, UserRegisterForm, MealPlanForm
from .models import MealPlan

from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.contrib.auth.decorators import login_required


def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)


# -------------------------
# Auth & Home Views
# -------------------------

def custom_logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')

@login_required
def meal_plan_list(request):
    breakfast = MealPlan.objects.filter(user=request.user, time_of_day='Breakfast').order_by('date')
    lunch = MealPlan.objects.filter(user=request.user, time_of_day='Lunch').order_by('date')
    dinner = MealPlan.objects.filter(user=request.user, time_of_day='Dinner').order_by('date')
    snack = MealPlan.objects.filter(user=request.user, time_of_day='Snack').order_by('date')
    
    return render(request, 'mylife/meal_plan_list.html', {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snack': snack,
    })

class HomeView(TemplateView):
    template_name = 'home.html'

class LogoutView(TemplateView):
    template_name = 'registration/logged_out.html'

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



@login_required
def weekly_calendar_view(request):
    # Parse target date from query param or use today
    date_str = request.GET.get('date')
    if date_str:
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            target_date = datetime.today().date()
    else:
        target_date = datetime.today().date()

    # Get the Sunday before (or on) the selected day
    start_of_week = target_date - timedelta(days=target_date.weekday() + 1 if target_date.weekday() != 6 else 0)
    week_days = [start_of_week + timedelta(days=i) for i in range(7)]  # Sunday to Saturday

    calendar_data = []
    for day in week_days:
        wellness = MyPlan.objects.filter(date=day).first()
        meals = MealPlan.objects.filter(user=request.user, date=day)

        # Break out meals by time_of_day
        meal_slots = {slot: "Open" for slot in ['Breakfast', 'Lunch', 'Dinner', 'Snack']}
        for meal in meals:
            meal_slots[meal.time_of_day] = meal.meal.name

        calendar_data.append({
            'date': day,
            'wellness': wellness,
            'meals': meal_slots
        })

    return render(request, 'mylife/weekly_calendar.html', {
        'calendar_data': calendar_data,
        'target_date': target_date,
    })

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import MyPlan

@login_required
def myplan_options_view(request, date):
    plan = MyPlan.objects.filter(user=request.user, date=date).first()
    if not plan:
        messages.error(request, "No plan found for that date.")
        return redirect('myplan_list')


    if request.method == 'POST':
        if 'delete' in request.POST:
            return render(request, 'mylife/myplan_list_update.html', {
                'plan': plan,
                'confirm_delete': True,
            })
        elif 'confirm_delete' in request.POST:
            plan.delete()
            messages.success(request, f"Plan for {date} deleted.")
            return redirect('myplan_list')
        elif 'update' in request.POST:
            return redirect('myplan_update', pk=plan.pk)

    return render(request, 'mylife/myplan_list_update.html', {
        'plan': plan,
        'confirm_delete': False,
    })



# -------------------------
# MyPlan Views
# -------------------------

class MyPlanListView(LoginRequiredMixin, ListView):
    model = MyPlan
    template_name = 'mylife/myplan_list.html'
    context_object_name = 'myplans'
    ordering = ['date']

    def get_queryset(self):
        return MyPlan.objects.filter(user=self.request.user).order_by('date')


class MyPlanDetailView(DetailView):
    model = MyPlan
    template_name = 'mylife/myplan_detail.html'

class MyPlanCreateView(LoginRequiredMixin, CreateView):
    model = MyPlan
    form_class = MyPlanForm
    template_name = 'mylife/myplan_form.html'
    success_url = reverse_lazy('myplan_list')

    def form_valid(self, form):
        # Ensure the logged-in user is assigned to the user field
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MyPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MyPlan
    form_class = MyPlanForm
    template_name = 'mylife/myplan_form.html'
    success_url = reverse_lazy('myplan_list')

class MyPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MyPlan
    template_name = 'mylife/myplan_confirm_delete.html'
    success_url = reverse_lazy('myplan_list')

# -------------------------
# Meal Views
# -------------------------

class MealListView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'mylife/meal_list.html'
    context_object_name = 'meals'

class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ['name']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = Meal
    fields = ['name']
    template_name = 'mylife/meal_form.html'
    success_url = reverse_lazy('meal_list')

class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'mylife/meal_confirm_delete.html'
    success_url = reverse_lazy('meal_list')

# -------------------------
# MealPlan Views
# -------------------------

@login_required
def create_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            meal_plan = form.save(commit=False)
            meal_plan.user = request.user
            meal_plan.save()
            return redirect('meal_plan_list')  # Make sure this name is in your urls.py
    else:
        form = MealPlanForm()
    return render(request, 'mylife/create_meal_plan.html', {'form': form})

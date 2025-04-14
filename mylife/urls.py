from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib import admin  # Import the admin module
from .views import (
    HomeView,
    MyPlanListView,
    MyPlanDetailView,
    MyPlanCreateView,
    MyPlanUpdateView,
    MyPlanDeleteView,
    MealListView,
    MealCreateView,
    MealUpdateView,
    MealDeleteView,
  
    
)
from .views import register
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's auth URLs
    path('', HomeView.as_view(), name='home'),
    path('registration/register/', register, name='register'),
    path('myplans/', MyPlanListView.as_view(), name='myplan_list'),
    path('myplans/<int:pk>/', MyPlanDetailView.as_view(), name='myplan_detail'),
    path('myplans/create/', MyPlanCreateView.as_view(), name='myplan_create'),
    path('myplans/<int:pk>/update/', MyPlanUpdateView.as_view(), name='myplan_update'),
    path('myplans/<int:pk>/delete/', MyPlanDeleteView.as_view(), name='myplan_delete'),
    path('meals/', MealListView.as_view(), name='meal_list'),
    path('meal/create/', MealCreateView.as_view(), name='meal_create'),
    path('meals/<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
    path('meals/<int:pk>/delete/', MealDeleteView.as_view(), name='meal_delete'),
    path('plan/new/', views.create_meal_plan, name='create_meal_plan'),
    path('plan/list/', views.meal_plan_list, name='meal_plan_list'),
    path('calendar/week/', views.weekly_calendar_view, name='weekly_calendar'),
    path('myplan/options/<str:date>/', views.myplan_options_view, name='myplan_options'),

]

handler400 = 'mylife.views.custom_400'
handler403 = 'mylife.views.custom_403'
handler404 = 'mylife.views.custom_404'
handler500 = 'mylife.views.custom_500'

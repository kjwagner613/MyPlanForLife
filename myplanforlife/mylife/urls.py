from django.urls import path
from . import views
from django.views.generic import TemplateView
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

    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('myplans/', MyPlanListView.as_view(), name='myplan_list'),
    path('myplans/<int:pk>/', MyPlanDetailView.as_view(), name='myplan_detail'),
    path('myplans/create/', MyPlanCreateView.as_view(), name='myplan_create'),
    path('myplans/<int:pk>/update/', MyPlanUpdateView.as_view(), name='myplan_update'),
    path('myplans/<int:pk>/delete/', MyPlanDeleteView.as_view(), name='myplan_delete'),
    path('meals/', MealListView.as_view(), name='meal_list'),
    path('meals/create/', MealCreateView.as_view(), name='meal_create'),
    path('meals/<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
    path('meals/<int:pk>/delete/', MealDeleteView.as_view(), name='meal_delete'),

]
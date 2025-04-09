from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import mealsListView, MealCreateView, MealUpdateView, MealDeleteView


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', TemplateView.as_view(template_name='mylife/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='mylife/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='mylife/contact.html'), name='contact'),
    path('meal/', views.meal, name='meal'),
    path('plan/', views.plan, name='plan'),
    path('meal/', mealsListView.as_view(), name='meals_list'),
    path('meal/create/', MealCreateView.as_view(), name='meal_create'),
    path('meal/<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
    path('meal/<int:pk>/delete/', MealDeleteView.as_view(), name='meal_delete'),

]
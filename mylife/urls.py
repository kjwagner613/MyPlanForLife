from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
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
    register,
    custom_logout_view,
    create_meal_plan,
    meal_plan_list,
    weekly_calendar_view,
    myplan_options_view,
    myplan_by_date_view,
)

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', custom_logout_view, name='logout'),
    path('admin/', admin.site.urls),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='home'),
    path('myplans/', MyPlanListView.as_view(), name='myplan_list'),
    path('myplans/<int:pk>/', MyPlanDetailView.as_view(), name='myplan_detail'),
    path('myplans/create/', MyPlanCreateView.as_view(), name='myplan_create'),
    path('myplans/<int:pk>/update/', MyPlanUpdateView.as_view(), name='myplan_update'),
    path('myplans/<int:pk>/delete/', MyPlanDeleteView.as_view(), name='myplan_delete'),
    path('meals/', MealListView.as_view(), name='meal_list'),
    path('meal/create/', MealCreateView.as_view(), name='meal_create'),
    path('meals/<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
    path('meals/<int:pk>/delete/', MealDeleteView.as_view(), name='meal_delete'),
    path('plan/new/', create_meal_plan, name='create_meal_plan'),
    path('plan/list/', meal_plan_list, name='meal_plan_list'),
    path('calendar/week/', weekly_calendar_view, name='weekly_calendar'),
    path('myplan/options/<str:date>/', myplan_options_view, name='myplan_options'),
    path('myplans/by-date/', myplan_by_date_view, name='myplan_by_date'),
]

handler400 = 'mylife.views.custom_400'
handler403 = 'mylife.views.custom_403'
handler404 = 'mylife.views.custom_404'
# handler500 = 'mylife.views.custom_500'

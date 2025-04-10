from django.contrib import admin
from .models import MyPlan, Meal

# Register your models here.
admin.site.register(MyPlan)
admin.site.register(Meal)
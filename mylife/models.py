from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.


class Meal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    MEAL_TIMES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    time_of_day = models.CharField(max_length=10, choices=MEAL_TIMES)

    def __str__(self):
        return f"{self.meal.name} for {self.time_of_day} on {self.date}"


from django.contrib.auth.models import User

def get_default_user():
    return User.objects.first().id  # Replace with logic to get the desired user

class MyPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    date = models.DateField(default=datetime.date.today)
    physical = models.CharField(max_length=255, default='Body Plan')
    spiritual = models.CharField(max_length=255, default='Spiritual Needs')
    emotional = models.CharField(max_length=255, default='Emotional Needs')
    mental = models.CharField(max_length=255, default='Support System')   
    quality = models.CharField(max_length=255, default='Fulfillment')
    goals = models.CharField(max_length=255, default='Future Aspirations')  

    def __str__(self):
        return f"MyPlan for {self.date}"
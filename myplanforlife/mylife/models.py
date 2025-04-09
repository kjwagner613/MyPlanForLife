from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100)
    mealtime = models.choices([
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ], default='Breakfast')

    def __str__(self):
        return self.name

class MyPlan(models.Model):
    reference = models.CharField(max_length=255, default='Enter Name or Number')
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    physical = models.CharField(max_length=255, default='Body Plan')
    spiritual = models.CharField(max_length=255, default='Spiritual Needs')
    emotional = models.CharField(max_length=255, default='Emotional Needs')
    mental = models.CharField(max_length=255, default='Support System')   
    quality = models.CharField(max_length=255, default='Fulfillment')
    goals = models.CharField(max_length=255, default='Future Aspirations')  


    def __str__(self):
        return self.name
    
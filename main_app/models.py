from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

# MODELS
MEAL = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
    ('S', 'Snack')
)


class Workout(models.Model):
    activity = models.CharField(max_length=100)
    howLong = models.IntegerField()
    description = models.TextField(max_length=300)
    time = models.DateTimeField('Workout Time', default=datetime.now(), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})


class Food(models.Model):
    date = models.DateTimeField('Meal Time', default=datetime.now(), blank=True)
    item = models.CharField(max_length=100)
    calories = models.IntegerField()
    meal = models.CharField(
        max_length=1,
        choices=MEAL,
        default=MEAL[0][0]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['-date']

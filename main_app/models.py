from django.db import models
from django.urls import reverse

# MODELS


class Workout(models.Model):
    activity = models.CharField(max_length=100)
    howLong = models.IntegerField()
    description = models.TextField(max_length=300)
    time = models.TimeField('Workout Time')

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})
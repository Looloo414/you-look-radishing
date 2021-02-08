from django.db import models

# MODELS 

class Workout: 
    def __init__(self, activity, howLong, description, time ):
        self.activity = activity
        self.howLong = howLong
        self.description = description
        self.time = time 

workouts = [
    Workout('Stretch', 5, 'Loosen Muscles', '5:30')
]


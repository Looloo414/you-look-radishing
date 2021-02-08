from django.shortcuts import render, redirect
from .models import Workout

# workouts = [
#   Workout('Stretch', 4, 'feelz guud'),
# ]

class Workout: 
    def __init__(self, activity, howLong, description, time ):
        self.activity = activity
        self.howLong = howLong
        self.description = description
        self.time = time 


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
  workouts = Workout.object.all()  
  return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request, workout_id):
    workout = Workout.object.all(id=workout_id)
from django.shortcuts import render, redirect
from .models import Workout

class Workout: 
    def __init__(self, activity, howLong, description, time ):
        self.activity = activity
        self.howLong = howLong
        self.description = description
        self.time = time 

# workouts = [
#     Workout('Stretch', 5, 'Loosen Muscles', '5:30'),
#     Workout('Pushups', 20, 'Push body up and down', '6:30')
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
  workouts = Workout.object.all()  
  return render(request, 'workouts/index.html', { 'workouts': workouts })
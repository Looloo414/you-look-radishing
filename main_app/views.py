from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Workout


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def workouts_index(request):
    workouts = Workout.object.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})


def workouts_detail(request, workout_id):
    workout = Workout.object.all(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})


class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'
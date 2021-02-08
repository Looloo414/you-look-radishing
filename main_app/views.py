from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout, Food


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

#  --------------WORKOUTS----------------
def workouts_index(request):
    workouts = Workout.object.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})


def workouts_detail(request, workout_id):
    workout = Workout.object.all(id=workout_id)
    return render(request, 'workouts/detail.html', {'workout': workout})


class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'
    success_url = '/workout/'

class WorkoutUpdate(UpdateView):
    model = Workout
    fields = ['activity', 'howLong', 'description', 'time']

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts/'

# ---------------FOOD DIARY----------------------

def food_index(request):
    foods = Food.object.all()
    return render(request, 'food/index.html', {'foods': foods})


def food_detail(request, food_id):
    food = Food.object.all(id=food_id)
    return render(request, 'food/detail.html', {'food': food})
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout, Food
from .forms import FoodForm


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
    return render(request, 'food/detail.html', {'food': food, 'food_form': food_form})
    
def add_food(request, user_id):
    form = FoodForm(request.POST)
    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.user_id = user_id
        new_food.save()
        return redirect('detail', user_id=user_id)


from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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


class FoodCreate(CreateView):
    model = Food
    fields = '__all__'
    success_url = '/food/'


class FoodUpdate(UpdateView):
    model = Food
    fields = ['date', 'item', 'description', 'calories', 'meal']


class FoodDelete(DeleteView):
    model = Food
    success_url = '/foods/'

# ----------------USER/SIGNUP/LOGIN----------------


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

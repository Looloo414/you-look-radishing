from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Workout, Food
from .forms import FoodForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

#  --------------WORKOUTS----------------

@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})

@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get()
    return render(request, 'workouts/detail.html', {'workout': workout})


class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['activity','howLong', 'description']
    success_url = '/workout/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['activity', 'howLong', 'description']


class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'

# ---------------FOOD DIARY----------------------

@login_required
def food_index(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'food/index.html', {'foods': foods})

@login_required
def food_detail(request, food_id):
    food = Food.objects.get()
    return render(request, 'food/detail.html', {'food': food, 'food_form': food_form})

@login_required
def add_food(request, user_id):
    form = FoodForm(request.POST)
    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.user_id = user_id
        new_food.save()
        return redirect('detail', user_id=user_id)


class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['item', 'calories', 'meal']
    success_url = '/food/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class FoodUpdate(LoginRequiredMixin,UpdateView):
    model = Food
    fields = ['date', 'item', 'description', 'calories', 'meal']


class FoodDelete(LoginRequiredMixin, DeleteView):
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
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     weight = models.IntegerField()
#     height = models.IntegerField()
#     age = models.IntegerField()
#     healthGoals = models.CharField(max_length=300)
#     healthConditions = models.CharField(max_length=300)

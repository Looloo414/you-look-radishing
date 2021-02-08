from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('workout/', views.workouts_index, name='index'),
    path('workouts/,int:workout_id>/', view.workouts_detail, name='detail')

]
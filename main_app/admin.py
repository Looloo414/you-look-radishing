from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Workout, Food

# Register your models here.
admin.site.register(Workout)
admin.site.register(Food)

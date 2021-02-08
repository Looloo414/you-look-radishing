# Generated by Django 3.1.5 on 2021-02-08 18:10

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_auto_20210208_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 8, 18, 10, 43, 83509), verbose_name='Workout Time'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

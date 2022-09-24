# Generated by Django 4.1 on 2022-09-24 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthday',
        ),
        migrations.AddField(
            model_name='profile',
            name='bdate',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]

# Generated by Django 4.1 on 2022-09-24 13:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_birthday_profile_bdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

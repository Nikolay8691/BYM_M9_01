# Generated by Django 4.1 on 2022-09-24 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_address_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, default='1'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
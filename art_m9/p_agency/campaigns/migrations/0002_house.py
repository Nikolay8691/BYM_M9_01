# Generated by Django 4.1 on 2022-08-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
                ('street_type', models.CharField(max_length=5)),
                ('street_name', models.CharField(max_length=64)),
                ('house_number', models.IntegerField()),
                ('qnt_apts', models.IntegerField()),
                ('qnt_strs', models.IntegerField()),
                ('campaigns', models.ManyToManyField(blank=True, related_name='c_objects', to='campaigns.campaign')),
            ],
        ),
    ]

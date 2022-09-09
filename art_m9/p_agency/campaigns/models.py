from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Supervisor(models.Model):
	first = models.CharField(max_length = 64)
	last = models.CharField(max_length = 64)
	nick = models.CharField(max_length = 64)
	email = models.EmailField(max_length = 64, blank = True)
	phone = models.CharField(max_length = 32, blank = True)

	def __str__(self):
		return f' {self.nick} email : {self.email} , phone : {self.phone}'

class Campaign(models.Model):
	title = models.CharField(max_length = 64)
	status = models.CharField(max_length = 1)
	supervisor = models.ForeignKey(Supervisor, on_delete = models.CASCADE, related_name = 'controled_by')
	creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'created_by', default = 1)

	def __str__(self):
		return f'title = {self.title} status:({self.status})'

class House(models.Model):
	city = models.CharField(max_length = 64)
	street_type = models.CharField(max_length = 5)
	street_name = models.CharField(max_length = 64)
	house_number = models.IntegerField()
	qnt_apts = models.IntegerField()
	qnt_strs = models.IntegerField()
	campaigns = models.ManyToManyField(Campaign, blank=True, related_name = 'c_objects')

	def __str__(self):
		return f'\n{self.city}\n {self.street_type} . {self.street_name} , {self.house_number}\n'

class Checkup(models.Model):
	campaign = models.ForeignKey(Campaign, on_delete = models.CASCADE, related_name = 'departures')
	house = models.ForeignKey(House, on_delete = models.CASCADE, related_name = 'arrivals')
	check_date = models.DateField()

	def __str__(self):
		house = f'{self.house.city}, {self.house.street_type}. {self.house.street_name}, {self.house.house_number}'
		return f'\ndate = {self.check_date} : {self.campaign.title} {house}'

class Apartment(models.Model):
	house = models.ForeignKey(House, on_delete = models.CASCADE, related_name = 'from_house')
	staircase = models.IntegerField()
	number = models.IntegerField()
	size = models.IntegerField()
	rooms = models.IntegerField()

	def __str__(self):
		return f'{self.house} - {self.staircase}, \n apart_# {self.number}, rooms {self.rooms}, {self.size} m*2'

class CheckupResults(models.Model):
	checkup = models.ForeignKey(Checkup, on_delete = models.CASCADE, related_name = 'reason')
	apart = models.ForeignKey(Apartment, on_delete = models.CASCADE, related_name = 'answer')
	c_date = models.DateTimeField(blank = True)

	open_door = models.BooleanField(default = False)

	opinion = models.CharField(max_length = 64, blank = True)
	c_name = models.CharField(max_length = 64, blank = True)
	c_phone = models.CharField(max_length = 64, blank = True)
	comments = models.TextField(blank = True)

	def __str__(self):
		return f'{self.checkup.campaign.title} {self.checkup.house.city} {self.c_date} open : {self.open_door}'

	class Meta:
		verbose_name = 'CheckupResults'
		verbose_name_plural = 'CheckupResults_list'
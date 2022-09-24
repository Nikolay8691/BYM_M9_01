from django.db import models
from datetime import date

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nick = models.CharField(max_length = 64)
	phone = models.CharField(max_length = 32)

	f_name = models.CharField(max_length = 64, default = '1')
	l_name = models.CharField(max_length = 64, default = '1')
	email = models.EmailField(default = 'c@ya.ru')
	
	sex = models.CharField(max_length = 32, default = '1')
	address = models.CharField(max_length = 100, default = '1')
	bdate = models.DateField(default = date.today)

	def __str__(self):
		return f' {self.nick} - phone : {self.phone}'
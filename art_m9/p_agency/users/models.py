from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nick = models.CharField(max_length = 64)
	phone = models.CharField(max_length = 32)

	def __str__(self):
		return f' {self.nick} - phone : {self.phone}'
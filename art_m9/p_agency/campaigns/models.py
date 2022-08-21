from django.db import models

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
	supervisor = models.ForeignKey(Supervisor, on_delete = models.CASCADE, related_name = 'made_by')

	def __str__(self):
		return f'title = {self.title} status:({self.status})'
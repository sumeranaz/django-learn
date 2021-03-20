from django.db import models

# Create your models here.

class contents(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	number = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30, null=True)
	date = models.DateField(max_length = 30, null=True)

	def __str__(self):
		return f'{self.first_name}{self.last_name}'
		

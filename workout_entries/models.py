from django.db import models
from django.contrib.auth.models import User

class GymEntry(models.Model):
	workout_name = models.CharField(max_length = 25)
	text = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return ("Entry # {}".format(self.id))	

	class Meta:
		verbose_name_plural = "GymEntries"	

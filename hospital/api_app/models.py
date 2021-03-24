from django.db import models
from datetime import datetime

# Create your models here.

class BedAvailability(models.Model):
	id = models.AutoField(primary_key=True) # will be treated as bed number
	type = models.CharField(max_length=30, null=False, blank=False)
	status = models.CharField(max_length=20, null=False, blank=False, default='FREE') # 1.) Free 2.) ALLOTED
	patient_name = models.CharField(max_length=100, null=True, blank=True, default="")
	alloted_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return f"{self.id} {self.type} ({self.status})"


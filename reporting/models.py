from django.db import models

class Event(models.Model):
	"""
	Describes an event
	"""
	description = models.CharField(max_length = 200)
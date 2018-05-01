from django.db import models
import datetime
from django.utils import timezone
from django.contrib.gis.db import models

class Category(models.Model):
	"""
	Describes a category. Has title and description.
	"""
	title = models.CharField(max_length=30, unique = True)
	description = models.CharField(max_length=200, default = '')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class EventState(models.Model):
	"""
	Describes the state of an event. Default value is to_validate. Other possible values are valid, solved.
	"""	 
	name = models.CharField(max_length = 30)

class Event(models.Model):
	"""
	Describes an event
	"""
	
	description = models.CharField(max_length = 200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	location = models.PointField(help_text="POINT(longitude latitude)")
	author = models.CharField(max_length = 30) # temporary field
	state = models.ForeignKey(EventState, on_delete=models.PROTECT, default = 1)
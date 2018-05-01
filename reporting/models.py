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
		
class Event(models.Model):
	"""
	Describes an event
	"""
	def get_default_category():
		return Category.objects.get_or_create(title = "default", created=datetime.datetime.now(tz=timezone.utc))[0].id

	description = models.CharField(max_length = 200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default = get_default_category)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	location = models.PointField(help_text="POINT(latitude longitude)")
	author = models.CharField(max_length = 30) # temporary field
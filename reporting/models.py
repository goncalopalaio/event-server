from django.db import models

class Category(models.Model):
	"""
	Describes a category. Has title and description.
	"""
	title = models.CharField(max_length=30, unique = True)
	description = models.CharField(max_length=200, default = '')
		
class Event(models.Model):
	"""
	Describes an event
	"""
	description = models.CharField(max_length = 200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default = lambda: Category.objects.get_or_create(title = "default")[0])
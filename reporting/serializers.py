from rest_framework import serializers
from .models import Event, Category

class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = Category
		fields= ('id', 'title', 'description')

class EventSerializer(serializers.ModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = Event
		fields= ('url','description', 'category', 'created', 'updated')
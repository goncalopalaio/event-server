from rest_framework import serializers
from .models import Event, EventState, Category

class CategorySerializer(serializers.ModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = Category
		fields= ('id', 'title', 'description')

class EventStateSerializer(serializers.ModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = EventState
		fields= ('url', 'name')

class EventSerializer(serializers.ModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = Event
		fields= ('url','description', 'category', 'created', 'updated', 'location', 'author', 'state')
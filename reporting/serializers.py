from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
	"""
	Serializer for events
	"""
	class Meta:
		model = Event
		fields= ('url','description')

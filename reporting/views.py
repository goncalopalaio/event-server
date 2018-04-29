from django.http import HttpResponse
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

def index(request):
    return HttpResponse("Hello from the default view.")

class EventViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows events to be viewed or edited
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer	
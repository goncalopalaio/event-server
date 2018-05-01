from django.http import HttpResponse
from rest_framework import viewsets
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer

def index(request):
    return HttpResponse("Hello from the default view.")

class EventViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows events to be viewed or edited
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows categories to be viewed or edited
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
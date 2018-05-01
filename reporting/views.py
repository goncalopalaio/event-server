from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer

def index(request):
    return HttpResponse("Hello from the default view.")

class EventViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows events to be viewed or edited
	"""
	serializer_class = EventSerializer
	queryset = Event.objects.all()

	def get_queryset(self):
		"""
		Overrides default behaviour to support filtering against query parameters
		"""
		queryset = Event.objects.all()
		
		category_id = self.request.query_params.get('category_id', None)
		if category_id is not None:
			queryset = queryset.filter(category_id = category_id)

		return queryset

class CategoryViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows categories to be viewed or edited
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


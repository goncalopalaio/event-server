from django.http import HttpResponse
from rest_framework import viewsets, generics
from django.contrib.gis.measure import D
from django.contrib.gis.geos import fromstr
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

		
		queryset = self.filter_by_distance(self.request.query_params, queryset)
		return queryset
	
	def filter_by_distance(self, query_params, queryset):
		# ignore missing parameters
		lat = self.request.query_params.get('lat', None)
		lon = self.request.query_params.get('lon', None)
		dist_km = self.request.query_params.get('dist_km', None)

		if lat is not None and lon is not None and dist_km is not None:
			# @note these fields should be validated further to ensure the point object can always be built and the distance is correct
			point = fromstr("POINT({} {})".format(lat, lon))
			if point.valid:
				queryset = queryset.filter(location__distance_lte = (point, D(km = dist_km)))

		return queryset


class CategoryViewSet(viewsets.ModelViewSet):
	"""
	Endpoint that allows categories to be viewed or edited
	"""
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


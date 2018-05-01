from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'events', views.EventViewSet)
router.register(r'states', views.EventStateViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
	path('', views.index, name='index'),
	url('v1/', include(router.urls))
]
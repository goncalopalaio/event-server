from django.contrib import admin
from .models import Event

# Models that are registered to appear in the admin interface
admin.site.register(Event)
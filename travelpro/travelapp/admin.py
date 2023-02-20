from django.contrib import admin

# Register your models here.
from .models import place, person

admin.site.register(place)
admin.site.register(person)
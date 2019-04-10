from django.contrib import admin
from .models import Consumer, Entrepreneur, Administrator, Location

admin.site.register(Consumer)
admin.site.register(Entrepreneur)
admin.site.register(Administrator)
admin.site.register(Location)
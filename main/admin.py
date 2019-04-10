from django.contrib import admin

from .models import Consumer, Entrepreneur, Administrator, Location, Point, Filter, Entr_Request, Admin_Request

admin.site.register(Entr_Request)
admin.site.register(Admin_Request)
admin.site.register(Filter)
admin.site.register(Point)
admin.site.register(Consumer)
admin.site.register(Entrepreneur)
admin.site.register(Administrator)
admin.site.register(Location)
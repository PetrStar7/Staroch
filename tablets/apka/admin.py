from django.contrib import admin

# Register your models here.
from .models import Tablet, Reservation

admin.site.register(Tablet)
admin.site.register(Reservation)
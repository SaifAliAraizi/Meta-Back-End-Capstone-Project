from django.contrib import admin
from .models import MenuItem
from .models import Booking

# Register your models here.
admin.site.register(Booking)
admin.site.register(MenuItem)
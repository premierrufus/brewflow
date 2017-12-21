from django.contrib import admin
from .models import Tank, Barrel, Beer

# Register your models here.

admin.site.register(Tank)
admin.site.register(Barrel)
admin.site.register(Beer)

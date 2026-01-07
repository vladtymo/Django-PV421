from django.contrib import admin

from barbers.models import Barber

class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']
    search_fields = ['name', 'position']
    list_filter = ['position']

# Register your models here.
admin.site.register(Barber, BarberAdmin)
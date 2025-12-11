from django.contrib import admin
from .models import FireIncident

@admin.register(FireIncident)
class FireIncidentAdmin(admin.ModelAdmin):
    list_display = ('cause', 'date','houses_burned')
    search_fields = ('cause',)
    list_filter = ('cause','date')

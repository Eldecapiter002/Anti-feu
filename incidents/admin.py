from django.contrib import admin
from .models import FireIncident, IncidentPhoto

class IncidentPhotoInline(admin.TabularInline):
    model = IncidentPhoto
    extra = 1

@admin.register(FireIncident)
class FireIncidentAdmin(admin.ModelAdmin):
    list_display = ('date','commune','quartier','cause','houses_burned')
    search_fields = ('commune','quartier','avenue','cause')
    list_filter = ('cause','commune','date')
    inlines = [IncidentPhotoInline]

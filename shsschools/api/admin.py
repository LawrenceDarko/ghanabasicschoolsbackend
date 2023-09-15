from django.contrib import admin
from .models import School

# Register your models here.
# admin.site.register(School)
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'district', 'location')
    search_fields = ('name', 'district', 'location', 'region')
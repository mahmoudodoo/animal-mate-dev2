from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import the ImportExportModelAdmin
from .models import Clinic

@admin.register(Clinic)
class ClinicAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('name', 'longitude', 'latitude', 'country', 'city')
    list_filter = ('country', 'city')
    search_fields = ('name', 'country', 'city')

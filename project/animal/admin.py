
from django.contrib import admin
from .models import Animal,AnimalImage, AnimalRequest
from import_export.admin import ImportExportModelAdmin


@admin.register(Animal)
class AnimalAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    # Define the list_display and other configurations for the Animal model here
    pass

@admin.register(AnimalImage)
class AnimalImageAdmin(ImportExportModelAdmin):  
    pass

@admin.register(AnimalRequest)
class AnimalRequestAdmin(ImportExportModelAdmin):  
    list_display = ['animal', 'status', 'date']
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import the ImportExportModelAdmin
from .models import Account, Room, Report

@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ['username', 'country', 'full_name', 'mobile_number']

@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    # Define the list_display and other configurations for the Room model here
    pass

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    # Define the list_display and other configurations for the Report model here
    pass

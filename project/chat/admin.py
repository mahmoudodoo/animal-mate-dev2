from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import the ImportExportModelAdmin
from .models import Message

@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('author', 'room', 'timestamp', 'read')
    list_filter = ('room', 'read')
    search_fields = ('author__username', 'room__name')

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import the ImportExportModelAdmin
from .models import PayoutRequest

@admin.register(PayoutRequest)
class PayoutRequestAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('user', 'date', 'status', 'amount')
    list_filter = ('status', 'user')
    search_fields = ('user__username',)

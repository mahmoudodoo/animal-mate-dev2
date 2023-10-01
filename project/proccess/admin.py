from django.contrib import admin
from import_export.admin import ImportExportModelAdmin  # Import the ImportExportModelAdmin
from .models import Connect, ConnectRate, Notification

class ConnectAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('sender_user', 'receiver_user', 'sender_animal', 'receiver_animal', 'date_created', 'status')
    list_filter = ('status', 'date_created')
    search_fields = ('sender_user__username', 'receiver_user__username')

class ConnectRateAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('user', 'rate', 'connect', 'date', 'preview_in_page')
    list_filter = ('rate', 'date', 'preview_in_page')
    search_fields = ('user__username', 'connect__sender_animal__name', 'connect__receiver_animal__name')

class NotificationAdmin(ImportExportModelAdmin):  # Inherit from ImportExportModelAdmin
    list_display = ('receiver', 'date', 'body', 'url', 'read', 'done', 'expiration_date')
    list_filter = ('read', 'done', 'date', 'expiration_date')
    search_fields = ('receiver__username', 'body')

admin.site.register(Notification, NotificationAdmin)
admin.site.register(Connect, ConnectAdmin)
admin.site.register(ConnectRate, ConnectRateAdmin)

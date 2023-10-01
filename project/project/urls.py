from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('account/', include('account.urls')),
    path('animal/', include('animal.urls')),
    path('chat/', include('chat.urls')),
    path('clinic/', include('clinic.urls')),
    path('payment/', include('payment.urls')),
    path('proccess/', include('proccess.urls')),
    
]

# Add URL patterns for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add URL patterns for serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

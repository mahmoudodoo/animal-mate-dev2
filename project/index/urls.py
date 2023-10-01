from django.urls import path
from . import views

urlpatterns = [
    # Your other URL patterns here

    path('', views.home, name='home'),
]

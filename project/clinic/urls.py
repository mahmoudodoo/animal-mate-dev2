# urls.py
from django.urls import path
from . import apis

urlpatterns = [
    path('api/clinics/', apis.ClinicListCreateView.as_view(), name='clinic-list-create'),
    path('api/clinics/<int:pk>/', apis.ClinicRetrieveView.as_view(), name='clinic-retrieve'),
]

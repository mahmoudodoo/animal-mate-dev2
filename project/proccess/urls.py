# urls.py
from django.urls import path
from . import apis

urlpatterns = [
    path('api/connects/', apis.ConnectListCreateView.as_view(), name='connect-list-create'),
    path('api/connects/<int:pk>/', apis.ConnectRetrieveView.as_view(), name='connect-retrieve'),
    path('api/connect-rates/', apis.ConnectRateListCreateView.as_view(), name='connectrate-list-create'),
    path('api/connect-rates/<int:pk>/', apis.ConnectRateRetrieveView.as_view(), name='connectrate-retrieve'),
    path('api/notifications/', apis.NotificationListCreateView.as_view(), name='notification-list-create'),
    path('api/notifications/<int:pk>/', apis.NotificationRetrieveView.as_view(), name='notification-retrieve'),
]

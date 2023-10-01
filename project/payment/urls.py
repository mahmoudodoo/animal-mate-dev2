# urls.py
from django.urls import path
from . import apis

urlpatterns = [
    path('api/payout-requests/', apis.PayoutRequestListCreateView.as_view(), name='payoutrequest-list-create'),
    path('api/payout-requests/<int:pk>/', apis.PayoutRequestRetrieveView.as_view(), name='payoutrequest-retrieve'),
]

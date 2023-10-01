# urls.py
from django.urls import path
from . import apis, views

urlpatterns = [
    path('api/animals/', apis.AnimalListCreateView.as_view(), name='animal-list-create'),
    path('api/animals/<int:pk>/', apis.AnimalDetailView.as_view(), name='animal-detail'),
    path('api/animal-prices/', apis.AnimalPriceForStripeListCreateView.as_view(), name='animal-price-list-create'),
    path('api/animal-prices/<int:pk>/', apis.AnimalPriceForStripeDetailView.as_view(), name='animal-price-detail'),
    path('api/animal-requests/', apis.AnimalRequestListCreateView.as_view(), name='animal-request-list-create'),
    path('api/animal-requests/<int:pk>/', apis.AnimalRequestDetailView.as_view(), name='animal-request-detail'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('edit_animal/<int:animal_id>/', views.edit_animal, name='edit_animal'),
    path('get_cities/', views.get_cities, name='get_cities'),
    path('animal_requasts/', views.animal_requasts, name='animal_requasts'),
    
]

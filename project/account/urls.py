from django.urls import path
from . import views
from . import apis

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile_wallet/', views.profile_wallet, name='profile_wallet'),
    path('profile_reviews/', views.profile_reviews, name='profile_reviews'),
    path('profile_orders/', views.profile_orders, name='profile_orders'),
    path('profile_my_settings/', views.profile_my_settings, name='profile_my_settings'),
    path('profile_home/', views.profile_home, name='profile_home'),
    path('edit_location/', views.edit_location, name='edit_location'),
    path('upload_profile_image/', views.upload_profile_image, name='upload_profile_image'),
    path('profile_fav_cats/', views.profile_fav_cats, name='profile_fav_cats'),
    path('delete_favorite_animal/<int:animal_id>', views.delete_favorite_animal, name='delete_favorite_animal'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('profile_ads/', views.profile_ads, name='profile_ads'),
    path('delete_animal/<int:animal_id>/', views.delete_animal, name='delete_animal'),
    path('profile_account_url/', views.profile_account_url, name='profile_account_url'),
    path('api/accounts/', apis.AccountListCreateView.as_view(), name='account-list-create'),
    path('api/accounts/<int:pk>/', apis.AccountDetailView.as_view(), name='account-detail'),
    path('api/rooms/', apis.RoomListCreateView.as_view(), name='room-list-create'),
    path('api/rooms/<int:pk>/', apis.RoomDetailView.as_view(), name='room-detail'),
    path('api/reports/', apis.ReportListCreateView.as_view(), name='report-list-create'),
    path('api/reports/<int:pk>/', apis.ReportDetailView.as_view(), name='report-detail'),

]


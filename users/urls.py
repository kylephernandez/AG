"""URL patterns for user management endpoints."""
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("profiles/", views.UserProfileListView.as_view(), name="profile-list"),
    path("profiles/<int:pk>/", views.UserProfileDetailView.as_view(), name="profile-detail"),
    path("wallets/", views.WalletIdentityListView.as_view(), name="wallet-list"),
]

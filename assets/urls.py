"""URL patterns for asset endpoints."""
from django.urls import path

from . import views

app_name = "assets"

urlpatterns = [
    path("", views.AssetListView.as_view(), name="asset-list"),
    path("<int:pk>/", views.AssetDetailView.as_view(), name="asset-detail"),
]

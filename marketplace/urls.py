"""URL routes for marketplace operations."""
from django.urls import path

from . import views

app_name = "marketplace"

urlpatterns = [
    path("listings/", views.ListingListView.as_view(), name="listing-list"),
    path("listings/<int:pk>/", views.ListingDetailView.as_view(), name="listing-detail"),
    path("trades/<int:pk>/", views.TradeRequestDetailView.as_view(), name="trade-detail"),
]

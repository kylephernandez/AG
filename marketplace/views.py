"""Views for marketplace flows."""
from __future__ import annotations

from django.views import generic

from .models import Listing, TradeRequest


class ListingListView(generic.ListView):
    model = Listing
    paginate_by = 20
    queryset = Listing.objects.select_related("asset", "seller")


class ListingDetailView(generic.DetailView):
    model = Listing
    queryset = Listing.objects.select_related("asset", "seller").prefetch_related("trade_requests")


class TradeRequestDetailView(generic.DetailView):
    model = TradeRequest
    queryset = TradeRequest.objects.select_related("listing", "requester").prefetch_related("items")

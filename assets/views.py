"""Views for asset discovery and management."""
from __future__ import annotations

from django.views import generic

from .models import DataAsset


class AssetListView(generic.ListView):
    model = DataAsset
    paginate_by = 20
    queryset = DataAsset.objects.select_related("owner").prefetch_related("tags")


class AssetDetailView(generic.DetailView):
    model = DataAsset
    queryset = DataAsset.objects.select_related("owner").prefetch_related("previews", "tags")

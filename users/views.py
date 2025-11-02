"""Views for the users app."""
from __future__ import annotations

from django.views import generic

from .models import UserProfile, WalletIdentity


class UserProfileListView(generic.ListView):
    """Public directory of user profiles."""

    model = UserProfile
    queryset = UserProfile.objects.select_related("user")
    paginate_by = 20


class UserProfileDetailView(generic.DetailView):
    """Detail page for a specific profile."""

    model = UserProfile
    queryset = UserProfile.objects.select_related("user").prefetch_related("consents")


class WalletIdentityListView(generic.ListView):
    """Lists wallet identities for administrative review."""

    model = WalletIdentity
    paginate_by = 50

"""Smoke tests for marketplace models."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from assets.models import DataAsset
from .models import Listing, TradeRequest


class TradeRequestTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username="seller")
        self.buyer = get_user_model().objects.create_user(username="buyer")
        self.asset = DataAsset.objects.create(
            owner=self.user,
            title="Dataset",
            description="Sample",
            modality="text",
            storage_uri="https://example.com/data",
            license="Custom",
            price=100,
            status="published",
        )
        self.listing = Listing.objects.create(
            asset=self.asset,
            seller=self.user,
            title="Dataset listing",
            summary="Great data",
            asking_price=100,
        )

    def test_trade_request_string(self) -> None:
        trade_request = TradeRequest.objects.create(listing=self.listing, requester=self.buyer)
        self.assertIn("Dataset listing", str(trade_request))

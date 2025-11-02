"""Smoke tests for the assets app."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import DataAsset


class DataAssetModelTests(TestCase):
    def test_string_representation(self) -> None:
        user = get_user_model().objects.create_user(username="creator")
        asset = DataAsset.objects.create(
            owner=user,
            title="Test Asset",
            description="Sample",
            modality="text",
            storage_uri="https://example.com/asset.txt",
            license="CC-BY",
            price=10,
        )
        self.assertEqual(str(asset), "Test Asset")

"""Marketplace domain models."""
from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone


class Listing(models.Model):
    """An asset listing on the marketplace."""

    asset = models.ForeignKey("assets.DataAsset", on_delete=models.CASCADE, related_name="listings")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=200)
    summary = models.TextField()
    asking_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class TradeRequest(models.Model):
    """Proposal for exchanging one or more assets or currency."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("declined", "Declined"),
        ("cancelled", "Cancelled"),
    ]

    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="trade_requests")
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trade_requests")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Trade request for {self.listing} by {self.requester}"


class TradeRequestItem(models.Model):
    """Individual asset or currency component of a trade request."""

    trade_request = models.ForeignKey(TradeRequest, on_delete=models.CASCADE, related_name="items")
    asset = models.ForeignKey("assets.DataAsset", on_delete=models.SET_NULL, null=True, blank=True, related_name="trade_items")
    currency_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Trade request item"

    def __str__(self) -> str:
        if self.asset:
            return f"Asset: {self.asset.title}"
        return f"Currency: {self.currency_amount}"


class SettlementRecord(models.Model):
    """Records the outcome of an accepted trade."""

    trade_request = models.OneToOneField(TradeRequest, on_delete=models.CASCADE, related_name="settlement")
    fulfilled_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="settlements_fulfilled")
    delivered_at = models.DateTimeField(null=True, blank=True)
    access_instructions = models.TextField(blank=True)
    escrow_reference = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Settlement for {self.trade_request_id}"


class Dispute(models.Model):
    """Dispute raised for a trade."""

    trade_request = models.ForeignKey(TradeRequest, on_delete=models.CASCADE, related_name="disputes")
    raised_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="disputes")
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("open", "Open"),
            ("in_review", "In review"),
            ("resolved", "Resolved"),
        ],
        default="open",
    )
    resolution = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Dispute for {self.trade_request_id} ({self.status})"

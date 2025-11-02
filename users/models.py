"""Database models for user identity and consent."""
from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone


class WalletIdentity(models.Model):
    """Links a user account to a cryptographic wallet address."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallets")
    address = models.CharField(max_length=128, unique=True)
    provider = models.CharField(max_length=64, help_text="Wallet provider or blockchain network identifier.")
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Wallet identities"

    def __str__(self) -> str:
        return f"{self.address} ({'verified' if self.verified else 'unverified'})"


class UserProfile(models.Model):
    """Extended profile metadata for AllGhost users."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=120, blank=True)
    avatar_url = models.URLField(blank=True, help_text="64x64 image used throughout the app.")
    bio = models.TextField(blank=True)
    public_metadata = models.JSONField(default=dict, blank=True)
    trust_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    consent_preference = models.CharField(
        max_length=32,
        choices=[
            ("open", "Open"),
            ("permissioned", "Permissioned"),
            ("private", "Private"),
        ],
        default="permissioned",
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["user__username"]

    def __str__(self) -> str:
        return self.display_name or self.user.get_username()


class ConsentPreference(models.Model):
    """Fine grained consent toggle for specific data handling categories."""

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="consents")
    category = models.CharField(max_length=100)
    is_enabled = models.BooleanField(default=True)
    notes = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("profile", "category")
        ordering = ["category"]

    def __str__(self) -> str:
        status = "enabled" if self.is_enabled else "disabled"
        return f"{self.profile} - {self.category} ({status})"


class ModeratorNote(models.Model):
    """Internal notes for moderators to document decisions."""

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="moderator_notes")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="authored_moderator_notes")
    note = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Note on {self.profile} by {self.author or 'system'}"

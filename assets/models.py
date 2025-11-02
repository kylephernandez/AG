"""Data asset models capturing multimodal content and metadata."""
from __future__ import annotations

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class AssetTag(models.Model):
    """Tag for categorising data assets."""

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class DataAsset(models.Model):
    """A multimodal asset published by a user."""

    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("restricted", "Restricted"),
        ("private", "Private"),
    ]

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("archived", "Archived"),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="data_assets")
    title = models.CharField(max_length=200)
    description = models.TextField()
    modality = models.CharField(max_length=50, help_text="Primary modality, e.g. text, image, audio, video, sensor.")
    storage_uri = models.URLField(help_text="Location of the securely stored asset payload.")
    thumbnail_uri = models.URLField(blank=True)
    license = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    visibility = models.CharField(max_length=12, choices=VISIBILITY_CHOICES, default="restricted")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="draft")
    tags = models.ManyToManyField(AssetTag, related_name="assets", blank=True)
    consent_restrictions = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["status", "visibility"])]

    def __str__(self) -> str:
        return self.title


class AssetPreview(models.Model):
    """Lightweight preview representation of an asset."""

    asset = models.ForeignKey(DataAsset, on_delete=models.CASCADE, related_name="previews")
    preview_type = models.CharField(
        max_length=32,
        choices=[
            ("thumbnail", "Thumbnail"),
            ("waveform", "Waveform"),
            ("transcript", "Transcript"),
            ("summary", "Summary"),
        ],
    )
    content = models.TextField(help_text="Preview payload or URI")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ("asset", "preview_type")

    def __str__(self) -> str:
        return f"{self.asset.title} ({self.preview_type})"


class AssetAccessRule(models.Model):
    """Defines who can request or view an asset."""

    asset = models.ForeignKey(DataAsset, on_delete=models.CASCADE, related_name="access_rules")
    rule_type = models.CharField(
        max_length=32,
        choices=[
            ("allow_role", "Allow role"),
            ("allow_user", "Allow specific user"),
            ("deny_user", "Deny specific user"),
            ("geo", "Geographic restriction"),
        ],
    )
    value = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Asset access rule"
        verbose_name_plural = "Asset access rules"

    def __str__(self) -> str:
        return f"{self.rule_type}: {self.value}"


class AssetAnalyticsSnapshot(models.Model):
    """Aggregated analytics metrics for a data asset."""

    asset = models.ForeignKey(DataAsset, on_delete=models.CASCADE, related_name="analytics")
    date = models.DateField()
    views = models.PositiveIntegerField(default=0)
    requests = models.PositiveIntegerField(default=0)
    trades = models.PositiveIntegerField(default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        unique_together = ("asset", "date")
        ordering = ["-date"]

    def __str__(self) -> str:
        return f"Analytics for {self.asset} on {self.date}"

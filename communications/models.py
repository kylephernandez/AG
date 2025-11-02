"""Messaging and notification models."""
from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone


class Conversation(models.Model):
    """Conversation can be a direct message or a cluster chat."""

    CONVERSATION_TYPES = [
        ("direct", "Direct"),
        ("cluster", "Cluster"),
    ]

    title = models.CharField(max_length=200, blank=True)
    conversation_type = models.CharField(max_length=20, choices=CONVERSATION_TYPES)
    topic = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title or f"{self.conversation_type} conversation #{self.pk}"


class ConversationParticipant(models.Model):
    """Links users to conversations with role metadata."""

    ROLE_CHOICES = [
        ("member", "Member"),
        ("moderator", "Moderator"),
        ("observer", "Observer"),
    ]

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="participants")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="conversations")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    joined_at = models.DateTimeField(default=timezone.now)
    last_read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("conversation", "user")

    def __str__(self) -> str:
        return f"{self.user} in {self.conversation}"


class Message(models.Model):
    """Message sent within a conversation."""

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_messages")
    body = models.TextField()
    attachment_uri = models.URLField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    edited_at = models.DateTimeField(null=True, blank=True)
    is_system = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return f"Message {self.pk} in {self.conversation}"


class Notification(models.Model):
    """Notification for a user."""

    CATEGORY_CHOICES = [
        ("trade", "Trade"),
        ("message", "Message"),
        ("system", "System"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    payload = models.JSONField(default=dict)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Notification {self.pk} for {self.user}"


class PresenceRecord(models.Model):
    """Tracks when a user was last active."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="presence")
    last_seen_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=[
            ("online", "Online"),
            ("away", "Away"),
            ("offline", "Offline"),
        ],
        default="offline",
    )

    def __str__(self) -> str:
        return f"{self.user} is {self.status}"

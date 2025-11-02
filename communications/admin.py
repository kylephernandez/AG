"""Admin registrations for communications."""
from django.contrib import admin

from .models import Conversation, ConversationParticipant, Message, Notification, PresenceRecord


class ConversationParticipantInline(admin.TabularInline):
    model = ConversationParticipant
    extra = 0


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "conversation_type", "title", "created_at", "is_archived")
    list_filter = ("conversation_type", "is_archived")
    inlines = [ConversationParticipantInline, MessageInline]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "is_read", "created_at")
    list_filter = ("category", "is_read")


@admin.register(PresenceRecord)
class PresenceRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "status", "last_seen_at")


admin.site.register(Message)
admin.site.register(ConversationParticipant)

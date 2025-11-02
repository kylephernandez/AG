"""Views supporting communications endpoints."""
from __future__ import annotations

from django.views import generic

from .models import Conversation, Message, Notification


class ConversationListView(generic.ListView):
    model = Conversation
    paginate_by = 20
    queryset = Conversation.objects.prefetch_related("participants")


class ConversationDetailView(generic.DetailView):
    model = Conversation
    queryset = Conversation.objects.prefetch_related("participants", "messages")


class NotificationListView(generic.ListView):
    model = Notification
    paginate_by = 50


class MessageDetailView(generic.DetailView):
    model = Message
    queryset = Message.objects.select_related("conversation", "sender")

"""Smoke tests for communications models."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Conversation, ConversationParticipant, Message


class ConversationTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username="user1")
        self.other = get_user_model().objects.create_user(username="user2")
        self.conversation = Conversation.objects.create(conversation_type="direct")
        ConversationParticipant.objects.create(conversation=self.conversation, user=self.user)
        ConversationParticipant.objects.create(conversation=self.conversation, user=self.other)

    def test_message_string(self) -> None:
        message = Message.objects.create(conversation=self.conversation, sender=self.user, body="Hello")
        self.assertIn("Message", str(message))

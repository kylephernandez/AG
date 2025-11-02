"""Smoke tests for the users app."""
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import UserProfile


class UserProfileModelTests(TestCase):
    def test_profile_string_representation(self) -> None:
        user = get_user_model().objects.create_user(username="alice")
        profile = UserProfile.objects.create(user=user, display_name="Alice")
        self.assertEqual(str(profile), "Alice")

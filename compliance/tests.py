"""Smoke tests for compliance models."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import AuditLog, Report


class AuditLogTests(TestCase):
    def test_str(self) -> None:
        user = get_user_model().objects.create_user(username="moderator")
        log = AuditLog.objects.create(actor=user, action="login")
        self.assertIn("login", str(log))


class ReportTests(TestCase):
    def test_report_string(self) -> None:
        user = get_user_model().objects.create_user(username="reporter")
        report = Report.objects.create(reporter=user, description="Issue")
        self.assertIn("Report", str(report))

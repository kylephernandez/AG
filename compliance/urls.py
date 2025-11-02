"""URL patterns for compliance tooling."""
from django.urls import path

from . import views

app_name = "compliance"

urlpatterns = [
    path("audit-logs/", views.AuditLogListView.as_view(), name="audit-log-list"),
    path("reports/", views.ReportListView.as_view(), name="report-list"),
]

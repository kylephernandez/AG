"""Views for compliance dashboards."""
from __future__ import annotations

from django.views import generic

from .models import AuditLog, Report


class AuditLogListView(generic.ListView):
    model = AuditLog
    paginate_by = 50


class ReportListView(generic.ListView):
    model = Report
    paginate_by = 50
    queryset = Report.objects.select_related("reporter", "target_user")

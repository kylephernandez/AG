"""Admin registrations for compliance."""
from django.contrib import admin

from .models import AuditLog, KYCVerification, ModerationAction, Report


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ("action", "actor", "created_at", "ip_address")
    list_filter = ("action",)
    search_fields = ("action", "actor__username")
    readonly_fields = ("created_at",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "reporter", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("reporter__username", "description")
    readonly_fields = ("created_at", "updated_at")


@admin.register(ModerationAction)
class ModerationActionAdmin(admin.ModelAdmin):
    list_display = ("report", "moderator", "action_type", "created_at")
    search_fields = ("report__id", "moderator__username", "action_type")
    readonly_fields = ("created_at",)


@admin.register(KYCVerification)
class KYCVerificationAdmin(admin.ModelAdmin):
    list_display = ("user", "provider", "status", "submitted_at")
    list_filter = ("status", "provider")
    search_fields = ("user__username", "reference_id")
    readonly_fields = ("submitted_at", "updated_at")

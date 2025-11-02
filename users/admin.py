"""Admin registrations for the users app."""
from django.contrib import admin

from .models import ConsentPreference, ModeratorNote, UserProfile, WalletIdentity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "display_name", "trust_score", "consent_preference", "created_at")
    list_filter = ("consent_preference", "trust_score")
    search_fields = ("user__username", "display_name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(WalletIdentity)
class WalletIdentityAdmin(admin.ModelAdmin):
    list_display = ("user", "address", "provider", "verified", "created_at")
    list_filter = ("provider", "verified")
    search_fields = ("address", "user__username")
    readonly_fields = ("created_at",)


@admin.register(ConsentPreference)
class ConsentPreferenceAdmin(admin.ModelAdmin):
    list_display = ("profile", "category", "is_enabled", "updated_at")
    list_filter = ("is_enabled",)
    search_fields = ("profile__user__username", "category")
    readonly_fields = ("updated_at",)


@admin.register(ModeratorNote)
class ModeratorNoteAdmin(admin.ModelAdmin):
    list_display = ("profile", "author", "created_at")
    search_fields = ("profile__user__username", "author__username", "note")
    readonly_fields = ("created_at",)

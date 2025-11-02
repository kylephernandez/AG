"""Admin configuration for assets."""
from django.contrib import admin

from .models import AssetAccessRule, AssetAnalyticsSnapshot, AssetPreview, AssetTag, DataAsset


class AssetPreviewInline(admin.TabularInline):
    model = AssetPreview
    extra = 0


class AssetAccessRuleInline(admin.TabularInline):
    model = AssetAccessRule
    extra = 0


@admin.register(DataAsset)
class DataAssetAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "modality", "price", "status", "visibility", "created_at")
    list_filter = ("status", "visibility", "modality")
    search_fields = ("title", "description", "owner__username")
    date_hierarchy = "created_at"
    filter_horizontal = ("tags",)
    inlines = [AssetPreviewInline, AssetAccessRuleInline]


@admin.register(AssetTag)
class AssetTagAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(AssetAnalyticsSnapshot)
class AssetAnalyticsSnapshotAdmin(admin.ModelAdmin):
    list_display = ("asset", "date", "views", "requests", "trades", "revenue")
    list_filter = ("date",)


admin.site.register(AssetPreview)
admin.site.register(AssetAccessRule)

"""Admin registrations for marketplace entities."""
from django.contrib import admin

from .models import Dispute, Listing, SettlementRecord, TradeRequest, TradeRequestItem


class TradeRequestItemInline(admin.TabularInline):
    model = TradeRequestItem
    extra = 0


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "seller", "asking_price", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title", "seller__username", "summary")
    date_hierarchy = "created_at"


@admin.register(TradeRequest)
class TradeRequestAdmin(admin.ModelAdmin):
    list_display = ("listing", "requester", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("listing__title", "requester__username")
    inlines = [TradeRequestItemInline]


@admin.register(SettlementRecord)
class SettlementRecordAdmin(admin.ModelAdmin):
    list_display = ("trade_request", "fulfilled_by", "delivered_at", "escrow_reference")
    search_fields = ("trade_request__listing__title", "escrow_reference")


@admin.register(Dispute)
class DisputeAdmin(admin.ModelAdmin):
    list_display = ("trade_request", "raised_by", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("trade_request__listing__title", "raised_by__username", "reason")

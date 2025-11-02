"""URL patterns for communication features."""
from django.urls import path

from . import views

app_name = "communications"

urlpatterns = [
    path("conversations/", views.ConversationListView.as_view(), name="conversation-list"),
    path("conversations/<int:pk>/", views.ConversationDetailView.as_view(), name="conversation-detail"),
    path("notifications/", views.NotificationListView.as_view(), name="notification-list"),
    path("messages/<int:pk>/", views.MessageDetailView.as_view(), name="message-detail"),
]

"""Project level URL routing for AllGhost."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("users.urls")),
    path("api/assets/", include("assets.urls")),
    path("api/marketplace/", include("marketplace.urls")),
    path("api/comms/", include("communications.urls")),
    path("api/compliance/", include("compliance.urls")),
]

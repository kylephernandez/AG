"""Core project-level views for AllGhost."""
from django.http import JsonResponse


def index(request):
    """Return a minimal health response for the root endpoint."""
    return JsonResponse(
        {
            "name": "AllGhost API",
            "status": "ok",
            "endpoints": {
                "users": "/api/users/",
                "assets": "/api/assets/",
                "marketplace": "/api/marketplace/",
                "communications": "/api/comms/",
                "compliance": "/api/compliance/",
            },
        }
    )

"""Project level tests."""
from django.test import TestCase
from django.urls import reverse


class RootEndpointTests(TestCase):
    """Validate the project root endpoint returns a helpful response."""

    def test_root_endpoint_returns_health_payload(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
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
            },
        )

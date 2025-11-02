"""ASGI config for AllGhost."""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allghost.settings")

application = get_asgi_application()

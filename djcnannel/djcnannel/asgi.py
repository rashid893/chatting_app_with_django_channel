"""
ASGI config for djcnannel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""



import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import home.routing
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djcnannel.settings')

# application = get_asgi_application()Normal


application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  'websocket': AuthMiddlewareStack(URLRouter(
    home.routing.websocket_urlpatterns
  ))
})
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     'websocket': URLRouter(
# 		home.routing.websocket_urlpatterns
# 	)

#     # Just HTTP for now. (We can add other protocols later.)
# })


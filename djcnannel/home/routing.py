from django.urls import path
from . import consumer
from django.conf.urls import url
#import from channels.security.websocket 

websocket_urlpatterns = [
  path('ws/sc/<str:groupkaname>/', consumer.MySyncConsumer.as_asgi()),
  path('ws/ac/', consumer.MyAsyncConsumer.as_asgi()),
]
#ws://127.0.0.1:8000/ws/sc/
from django.urls import path
import consumers

websocket_urlpatterns = [
    path("chat/", consumers.ChatConsumer.as_asgi()),
]
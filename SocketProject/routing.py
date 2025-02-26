
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from chat.consumer import ChatConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        re_path('ws/chat/', ChatConsumer.as_asgi()),
    ]),
})
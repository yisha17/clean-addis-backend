
from django.urls import re_path
from django.conf.urls import url
from . import consumers


websocket_url = [
    url(r'ws/notification/',consumers.NotificationConsumer.as_asgi())
]
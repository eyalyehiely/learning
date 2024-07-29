from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'/codeblock/ws(?P<codeblock_id>\d+)/$', consumers.CodeBlockConsumer.as_asgi()),
]

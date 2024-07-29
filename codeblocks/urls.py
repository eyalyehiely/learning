
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lobbyPage/',lobby_page, name="lobby page"),
    path('codeblock/<int:code_block_id>/',get_code_block,name="get code block")
]
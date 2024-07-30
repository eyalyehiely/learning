
from django.urls import path, include
from .views import *

urlpatterns = [
    path('lobbyPage/',get_code_blocks, name="code_locks"),
    path('codeblock/<int:code_block_id>/',get_code_block,name="get code block"),
    path('check/',check_user_code,name="check_user_code")
]
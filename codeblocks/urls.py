
from django.urls import path, include
from .views import *

urlpatterns = [
    path('codeblocks/',get_code_blocks, name="code_locks"),
    path('codeblock/<int:code_block_id>/',get_code_block,name="get code block"),
    path('codeblock/<int:code_block_id>/check/',check_user_code,name="check_user_code"),
    path('codeblock/<int:code_block_id>/edit/', edit_code_block, name='edit_code_block'),
]
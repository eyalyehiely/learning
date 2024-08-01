from django.urls import path
from .views import *

urlpatterns = [
    path('codeblocks/', get_code_blocks, name="code_locks"),
    path('codeblock/<int:code_block_id>/check/', check_user_code, name="check_user_code"),
    path("codeblock/submission/", codeblock_submission, name="codeblock_submission"),
    path("codeblock/submission/<int:code_block_id>/", codeblock_submission_detail, name="codeblock_submission_detail"),
    path("fetchClientUuidtoServer/", fetch_client_uuid_to_server, name='fetch_client_uuid_to_server'),
    path("codeblock/submission/<int:code_block_id>/edit/", edit_submission, name="edit_submission"),
    path('log_visitor/', log_visitor, name='log_visitor'),

]

from django.urls import path, include
from .views import *

urlpatterns = [
    path('codeblocks/', get_code_blocks, name="code_locks"),
    path('codeblock/<int:code_block_id>/check/', check_user_code, name="check_user_code"),
    path("codeblock/submission/<uuid:user_id>/", codeblock_submission, name="codeblock_submission"),
    path("codeblock/submission/<int:submission_id>/", codeblock_submission_detail, name="codeblock_submission_detail"),
]

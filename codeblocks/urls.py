from django.urls import path
from .views import get_code_blocks, check_user_code, codeblock_submission, codeblock_submission_detail

urlpatterns = [
    path('codeblocks/', get_code_blocks, name="code_locks"),
    path('codeblock/<int:code_block_id>/check/', check_user_code, name="check_user_code"),
    path("codeblock/submission/<uuid:user_id>/", codeblock_submission, name="codeblock_submission"),
    path("codeblock/submission/<int:code_block_id>/", codeblock_submission_detail, name="codeblock_submission_detail"),
]

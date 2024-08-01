from django.contrib import admin
from.models import *

class CodeBlockAdmin(admin.ModelAdmin):
    list_display = ('id','title','instructions','code','solution')
admin.site.register(CodeBlock, CodeBlockAdmin)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user_id','code_block','user_code','passed','created_at')
admin.site.register(Submission, SubmissionAdmin)
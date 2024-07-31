from django.contrib import admin
from.models import *

class CodeBlockAdmin(admin.ModelAdmin):
    list_display = ('id','title','instructions','code')
admin.site.register(CodeBlock, CodeBlockAdmin)


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user','code_block','user_code','passed','created_at')
admin.site.register(Submission, SubmissionAdmin)
from django.contrib import admin
from.models import CodeBlock

class CodeBlockAdmin(admin.ModelAdmin):
    list_display = ('id','title','instructions','code','solution')
admin.site.register(CodeBlock, CodeBlockAdmin)

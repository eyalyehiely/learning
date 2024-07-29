from django.contrib import admin
from.models import CodeBlock

class CodeBlockAdmin(admin.ModelAdmin):
    list_display = ('id','title','code','solution')
admin.site.register(CodeBlock, CodeBlockAdmin)

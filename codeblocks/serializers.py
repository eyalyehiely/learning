from rest_framework import serializers
from .models import CodeBlock

class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = '__all__'

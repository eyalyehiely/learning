from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import CodeBlock, Submission

class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = ['id', 'title', 'instructions', 'code']

class SubmissionSerializer(serializers.ModelSerializer):
    code_block_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Submission
        fields = ['code_block_id', 'user_id', 'user_code', 'passed', 'created_at']

    def create(self, validated_data):
        code_block_id = validated_data.pop('code_block_id')
        code_block = get_object_or_404(CodeBlock, id=code_block_id)
        submission = Submission.objects.create(code_block=code_block, **validated_data)
        return submission
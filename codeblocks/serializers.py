from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import CodeBlock, Submission

class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = ['id', 'title', 'instructions', 'code']

class SubmissionSerializer(serializers.ModelSerializer):
    code_block_id = serializers.IntegerField(write_only=True)
    code_block = serializers.PrimaryKeyRelatedField(queryset=CodeBlock.objects.all(), write_only=True)
    user_code = serializers.CharField()

    class Meta:
        model = Submission
        fields = ['code_block_id', 'user_id', 'user_code', 'passed', 'created_at', 'code_block']

    def create(self, validated_data):
        code_block_id = validated_data.pop('code_block_id')
        code_block = get_object_or_404(CodeBlock, id=code_block_id)
        submission = Submission.objects.create(code_block=code_block, **validated_data)
        return submission

    def update(self, instance, validated_data):
        instance.user_code = validated_data.get('user_code', instance.user_code)
        instance.passed = validated_data.get('passed', instance.passed)
        instance.save()
        return instance
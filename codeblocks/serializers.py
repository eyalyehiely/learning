from rest_framework import serializers
from .models import CodeBlock, Submission


class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        exclude = ['user_code']

    def create(self, validated_data):
        submission = Submission.objects.create(**validated_data)
        submission.save()
        submission.user_code = submission.code_block.code
        return submission

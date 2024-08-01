from django.db import models

class CodeBlock(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    code = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    code_block = models.ForeignKey(CodeBlock, on_delete=models.CASCADE)
    user_code = models.TextField()
    user_id = models.CharField(max_length=100)
    passed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Visitor(models.Model):
    client_uuid = models.CharField(max_length=100)
    url = models.URLField()
    visit_time = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.client_uuid} - {self.url}'
from django.db import models


class CodeBlock(models.Model):
    id = models.IntegerField(primary_key=True, editable=False,)
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    code = models.TextField()
    solution = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# Generated by Django 4.2.7 on 2024-08-01 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeblocks', '0005_visitor_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeblock',
            name='solution',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]

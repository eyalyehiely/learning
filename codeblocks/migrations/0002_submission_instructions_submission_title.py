# Generated by Django 5.0.7 on 2024-07-31 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeblocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='instructions',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='title',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]

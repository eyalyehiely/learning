# Generated by Django 4.1.5 on 2024-08-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeblocks', '0007_alter_codeblock_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeblock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

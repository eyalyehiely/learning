# Generated by Django 4.1.5 on 2024-08-01 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeblocks', '0006_codeblock_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeblock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.1.5 on 2023-05-08 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_noteapp_created_at_noteapp_modified_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="description",
            new_name="content",
        ),
    ]

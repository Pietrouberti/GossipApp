# Generated by Django 4.2.16 on 2024-11-02 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sources", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sources",
            old_name="vector_data",
            new_name="embedding",
        ),
        migrations.RenameField(
            model_name="sources",
            old_name="text_data",
            new_name="text",
        ),
    ]
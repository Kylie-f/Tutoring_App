# Generated by Django 4.2.16 on 2024-10-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0006_remove_tutor_friday_hours_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tutor",
            name="classes",
        ),
        migrations.AddField(
            model_name="tutor",
            name="classes",
            field=models.CharField(default="N/A", max_length=255),
        ),
    ]

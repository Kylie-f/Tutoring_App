# Generated by Django 4.2.16 on 2024-10-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_tutor_available_hours_tutor_suggested_classes"),
    ]

    operations = [
        migrations.AddField(
            model_name="tutor",
            name="fun_fact",
            field=models.CharField(default="No fun fact available", max_length=200),
        ),
        migrations.AddField(
            model_name="tutor",
            name="major",
            field=models.CharField(default="Undeclared", max_length=100),
        ),
    ]
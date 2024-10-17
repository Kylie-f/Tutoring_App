# Generated by Django 4.2.16 on 2024-10-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0003_class_remove_customuser_classes_remove_tutor_classes_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="tutor",
            name="available_hours",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="tutor",
            name="suggested_classes",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]
# Generated by Django 4.2.16 on 2024-10-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_remove_tutor_classes_tutor_classes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutor",
            name="classes",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0011_rename_foodimage_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="image", name="foods", field=models.JSONField(default={}),
        ),
    ]

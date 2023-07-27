# Generated by Django 4.2.3 on 2023-07-27 14:34

from django.db import migrations, models
import food.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        max_length=255, upload_to=food.utils.rename_imagefile_to_uuid
                    ),
                ),
                ("foods", models.JSONField(default={"foods": ["apple", "tomato"]})),
            ],
        ),
    ]

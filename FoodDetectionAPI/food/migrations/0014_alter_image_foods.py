# Generated by Django 4.2.3 on 2023-07-20 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0013_alter_image_foods"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="foods",
            field=models.JSONField(default={"foods": ["apple", "tomato"]}),
        ),
    ]

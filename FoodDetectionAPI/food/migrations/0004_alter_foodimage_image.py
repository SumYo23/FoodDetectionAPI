# Generated by Django 4.2.3 on 2023-07-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0003_alter_foodimage_image_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodimage",
            name="image",
            field=models.ImageField(upload_to="2023-07-18 16:51:30.717645"),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0005_alter_foodimage_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodimage",
            name="image",
            field=models.ImageField(upload_to="%Y%m%d507181133553526622"),
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0007_alter_foodimage_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="foodimage", name="food",),
        migrations.AlterField(
            model_name="foodimage",
            name="image",
            field=models.ImageField(upload_to="2023_07_18_17_06681824733410756178"),
        ),
        migrations.AddField(
            model_name="foodimage",
            name="food",
            field=models.ManyToManyField(to="food.food"),
        ),
    ]
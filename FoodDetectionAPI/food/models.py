from datetime import datetime

from django.db import models
import random

# Create your models here.
from food.utils import rename_imagefile_to_uuid


class FoodImage(models.Model):
    image = models.ImageField(upload_to=rename_imagefile_to_uuid, max_length=255)
    food = models.ManyToManyField("Food")


class Food(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=15, unique=True)
    foods = models.ManyToManyField("Food")

    def __str__(self):
        return self.name

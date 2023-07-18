from datetime import datetime

from django.db import models
import random


# Create your models here.
class FoodImage(models.Model):
    random_name = str(datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M")) + str(random.randint(1, 1000000000000000000))
    image = models.ImageField(upload_to=random_name)
    food = models.ManyToManyField("Food")

    def __str__(self):
        return self.random_name


class Food(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=15, unique=True)
    foods = models.ManyToManyField("Food")

    def __str__(self):
        return self.name

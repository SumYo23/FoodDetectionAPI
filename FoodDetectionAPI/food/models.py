from datetime import datetime

from django.db import models
import random

# Create your models here.
from food.utils import rename_imagefile_to_uuid


class Image(models.Model):
    image = models.ImageField(upload_to=rename_imagefile_to_uuid, max_length=255)
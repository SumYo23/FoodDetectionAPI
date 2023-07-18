from django.contrib import admin

# Register your models here.
from food.models import User, Food, FoodImage

admin.site.register(User)
admin.site.register(Food)
admin.site.register(FoodImage)

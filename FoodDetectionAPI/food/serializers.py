from rest_framework import serializers

from food.models import FoodImage, Food, User


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    food = FoodSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = FoodImage
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

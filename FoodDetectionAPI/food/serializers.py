from rest_framework import serializers

from food.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    foods = serializers.JSONField(required=False)

    class Meta:
        model = Image
        fields = "__all__"

from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classifier.classifier import predict
from food.models import Image
from food.serializers import ImageSerializer


class FoodImageList(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # POST로 얻은 id값과 image 경로 저장
            id = serializer.data.get("id")
            image = serializer.data.get("image")

            # AI모델에 이미지 경로를 넣어서, 어떤 음식인지 리스트 형태로 받아서 저장
            predict_result = predict(image)
            food_image = Image.objects.get(id=id)
            # for i in predict_result:
            #     food, _ = Food.objects.get_or_create(name=i)
            #     food_image.food.add(food)
            food_image.save()

            # serializer.save() 후 db에 저장했기 때문에, 새로운 serializer 호출
            result_serializer = ImageSerializer(Image.objects.get(id=id))
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodImageDetail(APIView):
    def get(self, request, food_image_id):
        model = Image.objects.get(pk=food_image_id)
        serializer = ImageSerializer(model)
        return Response(serializer.data)

    def put(self, request, food_image_id):
        model = Image.objects.get(pk=food_image_id)
        serializer = ImageSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

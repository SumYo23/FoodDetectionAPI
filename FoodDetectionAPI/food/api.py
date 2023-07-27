import os
import shutil

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classifier.classifier import predict
from food.models import Image
from food.serializers import ImageSerializer


class ImageDetaction(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            '''POST로 얻은 id값과 image 경로 저장'''
            id = serializer.data.get("id")
            image_route = serializer.data.get("image")

            '''AI모델에 이미지 경로를 넣어서, 어떤 음식인지 리스트 형태로 받아서 저장'''
            image = Image.objects.get(id=id)
            image.foods = {"foods": predict(image_route)}
            image.save()

            '''serializer.save() 후 db에 저장했기 때문에, 새로운 serializer 호출'''
            image = Image.objects.get(id=id)
            result = ImageSerializer(image).data.get("foods")
            #shutil.rmtree("./runs")
            shutil.rmtree("./images")
            Image.objects.all().delete()
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

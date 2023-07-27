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

            image_route = serializer.data.get("image")
            result = {"foods": predict(image_route)}

            shutil.rmtree("./images")
            Image.objects.all().delete()

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetactionList(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            image_route = serializer.data.get("image")
            predict_result = predict(image_route)
            result = [{"name": i} for i in predict_result]

            shutil.rmtree("./images")
            Image.objects.all().delete()

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from classifier.classifier import predict
from food.models import User, Food, FoodImage
from food.serializers import UserSerializer, FoodSerializer, FoodImageSerializer


class UserList(APIView):
    def get(self, request):
        model = User.objects.all()
        serializer = UserSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, user_id):
        model = User.objects.get(pk=user_id)
        serializer = UserSerializer(model)
        return Response(serializer.data)

    def put(self, request, user_id):
        model = User.objects.get(pk=user_id)
        serializer = UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodList(APIView):
    def get(self, request):
        model = Food.objects.all()
        serializer = FoodSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data.get("name"))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodDetail(APIView):
    def get(self, request, food_id):
        model = Food.objects.get(pk=food_id)
        serializer = FoodSerializer(model)
        return Response(serializer.data)

    def put(self, request, food_id):
        model = Food.objects.get(pk=food_id)
        serializer = FoodSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodImageList(APIView):
    def get(self, request):
        model = FoodImage.objects.all()
        serializer = FoodImageSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            result = predict(serializer.data.get("image")) #리스트 형태
            food_image = FoodImage.objects.get(id=serializer.data.get("id"))
            for i in result:
                food, _ = Food.objects.get_or_create(name=i)
                food_image.food.add(food)
            food_image.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodImageDetail(APIView):
    def get(self, request, food_image_id):
        model = FoodImage.objects.get(pk=food_image_id)
        serializer = FoodImageSerializer(model)
        return Response(serializer.data)

    def put(self, request, food_image_id):
        model = FoodImage.objects.get(pk=food_image_id)
        serializer = FoodImageSerializer(model, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
URL configuration for FoodDetectionAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from FoodDetectionAPI import settings
from food.api import UserList, UserDetail, FoodList, FoodDetail, FoodImageList, FoodImageDetail

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path("user_list/", UserList.as_view(), name="user_list"),
                  path("user_list/<int:user_id>", UserDetail.as_view(), name="user_detail"),
                  path("food_list/", FoodList.as_view(), name="food_list"),
                  path("food_list/<int:food_id>", FoodDetail.as_view(), name="food_detail"),
                  path("food_image_list/", FoodImageList.as_view(), name="food_image_list"),
                  path("food_image_list/<int:food_id>", FoodImageDetail.as_view(), name="food_image_detail"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
from django.urls import path
from .views import (ProductList, ProductCreate, ProductDetail, BrandList, BrandCreate, BrandDetail,
                    CategoryList, CategoryCreate, CategoryDetail)


urlpatterns = [
    path('productlist/', ProductList.as_view()),
    path('productcreate/', ProductCreate.as_view()),
    path('product/<str:name>', ProductDetail.as_view()),
    path('brandlist/', BrandList.as_view()),
    path('brandcreate/', BrandCreate.as_view()),
    path('branddetail/<int:pk>', BrandDetail.as_view()),
    path('categorylist/', CategoryList.as_view()),
    path('categorycreate/', CategoryCreate.as_view()),
    path('categorydetail/<int:pk>', CategoryDetail.as_view()),
]
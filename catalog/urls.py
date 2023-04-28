from django.urls import path
from .views import ProductList, ProductDetail


urlpatterns = [
    # path('brandapi/', BrandAPIView.as_view()),
    # path('brand/<int:pk>/', )
    # path('sizeapi/', SizeView.as_view()),
    # path('categoryapi/', CategoryView.as_view()),
    path('productlist/', ProductList.as_view()),
    path('product/<str:name>', ProductDetail.as_view()),
]
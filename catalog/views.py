from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .filters import  ProductFilter
from .models import Brand, Size, Category, Product
from .serializers import BrandSerializer, SizeSerializer, CategorySerializer, ProductSerializer


# class BrandListView(generics.ListAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#

# class BrandAPIView(generics.ListCreateAPIView):
#     queryset = Brand.objects.all()
#     serializer_class = BrandSerializer
#     permission_classes = (IsAdminUser, )
#
#
# class SizeView(generics.ListCreateAPIView):
#     queryset = Size.objects.all()
#     serializer_class = SizeSerializer
#     permission_classes = (IsAdminUser, )
#
#
# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = (IsAdminUser, )


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    # filterset_class = ProductFilter


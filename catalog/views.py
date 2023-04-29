from django.http import Http404
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Product, Brand, Category, Size
from .serializers import ProductSerializer, BrandSerializer, CategorySerializer, SizeSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )


class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser, )


class ProductDetail(APIView):
    permission_classes = (IsAdminUser, )
    def get_object(self, name):
        try:
            return Product.objects.get(name='name')
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, name):
        product = Product.objects.get(name=name)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, name):
        product = self.get_object(name)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        product = self.get_object(name)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BrandList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (AllowAny, )


class BrandCreate(generics.CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = (IsAdminUser, )


class BrandDetail(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, name):
        try:
            return Brand.objects.get(name='name')
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, name):
        brand = Brand.objects.get(name=name)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, name):
        brand = self.get_object(name)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        brand = self.get_object(name)
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser, )


class CategoryDetail(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, name):
        try:
            return Category.objects.get(name='name')
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = Brand.objects.get(name=name)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, name):
        category = self.get_object(name)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        category = self.get_object(name)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




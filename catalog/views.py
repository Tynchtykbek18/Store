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

    def get_object(self, pk):
        try:
            return Brand.objects.get(pk='pk')
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        brand = Brand.objects.get(pk=pk)
        serializer = BrandSerializer(brand)
        return Response(serializer.data)

    def put(self, request, pk):
        brand = self.get_object(pk)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        brand = self.get_object(pk)
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

    def get_object(self, pk):
        try:
            return Category.objects.get(pk='pk')
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = Brand.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SizeView(generics.ListAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = (AllowAny, )


class SizeCreate(generics.CreateAPIView):
    serializer_class = SizeSerializer
    permission_classes = (IsAdminUser, )


class SizeDeatil(APIView):
    permission_classes = (IsAdminUser,)

    def get_object(self, pk):
        try:
            return Size.objects.get(pk=pk)
        except Size.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        size = Product.objects.get(pk=pk)
        serializer = ProductSerializer(size)
        return Response(serializer.data)

    def put(self, request, pk):
        size = self.get_object(pk)
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        size = self.get_object(pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



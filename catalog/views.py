import rest_framework
from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


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

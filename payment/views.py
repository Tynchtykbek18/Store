from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import PaymentMethod, PaymentTransaction
from .serializers import MethodSerializer, TransactionSerializer


class MethodList(generics.ListCreateAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = MethodSerializer
    permission_classes = (IsAdminUser, )


class MethodDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_object(self, pk):
        return PaymentMethod.objects.get(pk='pk')

    def get(self, request, pk):
        brand = PaymentMethod.objects.get(pk=pk)
        serializer = MethodSerializer(brand)
        return Response(serializer.data)


    serializer_class = MethodSerializer
    permission_classes = (IsAdminUser, )


class TransactionList(generics.ListCreateAPIView):
    queryset = PaymentTransaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser, )


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = (IsAdminUser, )
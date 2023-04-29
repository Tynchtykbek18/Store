from django.urls import path
from .views import MethodList, MethodDetail, TransactionList, TransactionDetail


urlpatterns = [
    path('paymentmethod/', MethodList.as_view()),
    path('paymentmethod/detail/<int:pk>', MethodDetail.as_view()),
    path('transactionlist/', TransactionList.as_view()),
    path('transaction/detail/<int:pk>', TransactionDetail.as_view()),
]
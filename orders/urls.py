from django.urls import path
from .views import OrderList, OrderDetail, OrderItemList, OrderItemDetail


urlpatterns = [
    path('orderlist/', OrderList.as_view()),
    path('orderdetail/<int:pk>', OrderDetail.as_view()),
    path('orderitem/', OrderItemList.as_view()),
    path('orderitem/detail/<int:pk>', OrderItemDetail.as_view()),

]
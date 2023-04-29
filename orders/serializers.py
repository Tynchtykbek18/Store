from django.db.models import Sum
from rest_framework import serializers
from .models import Order, OrderItem
from catalog.models import Product
from catalog.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product_price = serializers.SerializerMethodField()
    product_quantity = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_product_quantity(self, obj):
        item_quantity = obj.quantity
        product_quantity = obj.product.quantity

        if item_quantity <= product_quantity:
            obj.save()
            return{
                'status': 'success',
            }

        else:
            return{
                'status': 'fail',
            }
    def get_product_price(self, obj):
        price = obj.product.price
        items = obj.quantity

        return{
            'item_price': price,
            'item_quantity': items,
            'total': price * items,
        }


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'




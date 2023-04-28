from django.db.models import Sum
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_amount(self, obj):
        total_order = obj.items.aggregate(Sum('price'))['price__sum']
        total_order_items = obj.items.aggregate(Sum('quantity'))['quantity__sum']
        return {
            'order_total': total_order,
            'order_items_total': total_order_items,
            'grand_total': total_order * total_order_items
        }

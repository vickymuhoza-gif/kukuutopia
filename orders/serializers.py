from rest_framework import serializers
from .models import Order, OrderItem, BulkOrder, Booking


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'product_name', 'quantity', 'price']


class BulkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkOrder
        fields = ['id', 'order', 'event_date', 'special_instructions', 'advance_payment_required']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    bulk_details = BulkOrderSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'location', 'order_type', 'total_amount',
            'payment_status', 'order_status', 'delivery_distance',
            'created_at', 'items', 'bulk_details',
        ]
        read_only_fields = ['created_at']


class BookingSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    user_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'user_name', 'product', 'product_name', 'quantity', 'reserved_until', 'status']

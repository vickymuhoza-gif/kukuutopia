from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, OrderItem, BulkOrder, Booking
from .serializers import OrderSerializer, OrderItemSerializer, BulkOrderSerializer, BookingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'order_status', 'payment_status', 'order_type']


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order', 'product']


class BulkOrderViewSet(viewsets.ModelViewSet):
    queryset = BulkOrder.objects.all()
    serializer_class = BulkOrderSerializer
    permission_classes = [permissions.AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('-reserved_until')
    serializer_class = BookingSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'product', 'status']

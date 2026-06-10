from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'method', 'amount', 'transaction_reference', 'status', 'paid_at']
        read_only_fields = ['paid_at']

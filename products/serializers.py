from rest_framework import serializers
from .models import Product, Inventory


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    owner_name = serializers.CharField(source='owner.full_name', read_only=True)
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'unit', 'price', 'image',
            'status', 'is_active', 'category', 'category_name',
            'owner', 'owner_name', 'branch', 'branch_name', 'created_at',
        ]
        read_only_fields = ['created_at']
        extra_kwargs = {
            'owner': {'required': False, 'allow_null': True},
            'branch': {'required': False, 'allow_null': True},
        }


class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    managed_by_name = serializers.CharField(source='managed_by.full_name', read_only=True)
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Inventory
        fields = [
            'id', 'product', 'product_name', 'managed_by', 'managed_by_name',
            'branch', 'branch_name', 'quantity_available', 'cost_price',
            'expiry_date', 'added_at',
        ]
        read_only_fields = ['added_at']
        extra_kwargs = {
            'managed_by': {'required': False, 'allow_null': True},
            'branch': {'required': False, 'allow_null': True},
        }

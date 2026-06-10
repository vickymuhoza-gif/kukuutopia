from rest_framework import serializers
from .models import Product,Inventory

class ProductSerializer(serializers.ModelSerializer):
  category_name = serializers.CharField(
    source = 'category.name',
    read_only =  True
  )
  
  class Meta:
    model = Product
    fields = [
      'id',
      'name',
      'description',
      'unit',
      'price',
      'image',
      'is_active',
      'category',
      'category_name',
      'created_at',
    ]

class InventorySerializer(serializers.ModelSerializer):
  product_name = serializers.CharField(
    source = 'product.name',
    read_only = True
  )

  managed_by_name = serializers.CharField(
    source = 'managed_by.name',
    read_only=True
  )
  class Meta:
    model = Inventory
    fields = [
      'id',
      'product',
      'product_name',
      'managed_by',
      'managed_by_name',
      'quantity_available',
      'cost_price',
      'expiry_date',
      'added_at',
    ]
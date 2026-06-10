from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Product, Inventory
from .serializers import ProductSerializer,InventorySerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.filter(is_active=True)
  serializer_class = ProductSerializer
  permission_classes = [permissions.AllowAny]

  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['category']

  def perform_create(self,serializer):
    serializer.save()

class InventoryViewSet(viewsets.ModelViewSet):
  queryset = Inventory.objects.all()
  serializer_class = InventorySerializer
  permission_classes = [permissions.AllowAny]
  filterset_fields = ['product']

  def perform_create(self, serializer):
    serializer.save()
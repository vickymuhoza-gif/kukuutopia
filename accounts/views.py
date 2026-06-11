from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

from .models import User, Location, Contact, Notification, Branch
from .serializers import (
    UserSerializer, LocationSerializer, ContactSerializer,
    NotificationSerializer, BranchSerializer, BranchAssignManagerSerializer,
    ChangePasswordSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('full_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['post'], url_path='change-password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not check_password(serializer.validated_data['current_password'], user.password):
            return Response({'current_password': 'Incorrect password.'}, status=status.HTTP_400_BAD_REQUEST)
        user.password = __import__('django.contrib.auth.hashers', fromlist=['make_password']).make_password(
            serializer.validated_data['new_password']
        )
        user.save()
        return Response({'detail': 'Password changed successfully.'})


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('name')
    serializer_class = BranchSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['patch'], url_path='assign-manager')
    def assign_manager(self, request, pk=None):
        branch = self.get_object()
        serializer = BranchAssignManagerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=serializer.validated_data['stock_manager_id'])
        branch.stock_manager = user
        branch.save()
        return Response(BranchSerializer(branch).data)

    @action(detail=True, methods=['get'], url_path='stock')
    def stock(self, request, pk=None):
        from products.models import Inventory
        from products.serializers import InventorySerializer
        branch = self.get_object()
        inventory = Inventory.objects.filter(branch=branch)
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['user', 'notification_type', 'is_read']


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

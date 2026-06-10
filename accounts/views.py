from rest_framework import viewsets, permissions, generics

from .models import User, Location, Contact, Notification
from .serializers import (
    UserSerializer,
    LocationSerializer,
    ContactSerializer,
    NotificationSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('full_name')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('city')
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]


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

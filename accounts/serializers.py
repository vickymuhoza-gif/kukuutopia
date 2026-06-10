from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Location, Contact, Notification


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            'id',
            'city',
            'district',
            'address',
            'created_at',
        ]
        read_only_fields = ['created_at']


class ContactSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(
        source='user.full_name',
        read_only=True,
    )

    class Meta:
        model = Contact
        fields = [
            'id',
            'user',
            'user_name',
            'type',
            'message',
            'created_at',
        ]
        read_only_fields = ['created_at']


class UserSerializer(serializers.ModelSerializer):
    location_address = serializers.CharField(
        source='location.address',
        read_only=True,
    )
    contacts = ContactSerializer(many=True, read_only=True)
    notifications = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = [
            'id',
            'location',
            'location_address',
            'full_name',
            'phone',
            'email',
            'password',
            'role',
            'is_verified',
            'created_at',
            'contacts',
            'notifications',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'location': {'required': False, 'allow_null': True},
        }
        read_only_fields = ['created_at']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'user',
            'user_name',
            'title',
            'message',
            'notification_type',
            'is_read',
            'metadata',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

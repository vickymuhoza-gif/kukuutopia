from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

from .models import User, Location, Contact, Notification, Branch


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'city', 'district', 'address', 'created_at']
        read_only_fields = ['created_at']


class ContactSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'user', 'user_name', 'type', 'message', 'created_at']
        read_only_fields = ['created_at']


class UserSerializer(serializers.ModelSerializer):
    location_address = serializers.CharField(source='location.address', read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)
    notifications = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'location', 'location_address', 'full_name', 'phone',
            'email', 'password', 'role', 'is_verified', 'avatar', 'created_at',
            'contacts', 'notifications',
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


class BranchSerializer(serializers.ModelSerializer):
    stock_manager_name = serializers.CharField(source='stock_manager.full_name', read_only=True)
    location_name = serializers.CharField(source='location.city', read_only=True)

    class Meta:
        model = Branch
        fields = ['id', 'name', 'location', 'location_name', 'stock_manager', 'stock_manager_name', 'created_at']
        read_only_fields = ['created_at']


class BranchAssignManagerSerializer(serializers.Serializer):
    stock_manager_id = serializers.IntegerField()

    def validate_stock_manager_id(self, value):
        try:
            user = User.objects.get(pk=value)
            if user.role != 'stock_manager':
                raise serializers.ValidationError("User must have stock_manager role.")
            return value
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found.")


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data


class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name', read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'user_name', 'title', 'message',
            'notification_type', 'is_read', 'metadata', 'created_at', 'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

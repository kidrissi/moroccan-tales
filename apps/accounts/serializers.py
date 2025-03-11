from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    """Serializer for reading and updating user data."""
    
    class Meta:
        model = User
        fields = ("id", "username", "email", "bio", "avatar")
        read_only_fields = ("id",)


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for user registration (creating a new user)."""
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password", "password_confirm", "bio", "avatar")
    
    def validate(self, data):
        """Ensure the passwords match."""
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """Create a new user instance."""
        validated_data.pop("password_confirm")
        user = User.objects.create_user(**validated_data)
        return user

# Importing necessary modules for authentication and serializers
from django.contrib.auth import authenticate  # Used to verify credentials and authenticate the user
from rest_framework import serializers  # Provides tools to easily serialize/deserialize data for APIs
from .models import User  # Importing the custom User model

# Serializer for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Declaring a password field, ensuring it's write-only (it will not be included in serialized responses)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User  # Associating this serializer with the custom User model
        fields = ('username', 'email', 'password')  # Fields that will be serialized/deserialized

    # Overriding the create method to handle user creation
    def create(self, validated_data):
        # Create a new User instance but don't save it to the database yet
        user = User(
            username=validated_data['username'],  # Assign the validated username
            email=validated_data['email']  # Assign the validated email
        )
        # Set the password using Django's built-in password hashing mechanism
        user.set_password(validated_data['password'])
        # Save the user to the database
        user.save()
        return user  # Return the created user instance

# Serializer for user login/authentication
class LoginSerializer(serializers.Serializer):
    # Username and password fields that will be passed to the serializer during login
    username = serializers.CharField()
    password = serializers.CharField()

    # Custom validation method to authenticate the user with the provided credentials
    def validate(self, data):
        # Authenticate the user using the provided username and password
        user = authenticate(**data)
        # If authentication fails, raise a validation error with a custom message
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user  # If successful, return the authenticated user

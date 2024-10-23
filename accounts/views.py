from rest_framework import generics  # Import generic views from Django REST Framework
from rest_framework.response import Response  # Import Response class to return responses
from .serializers import RegisterSerializer, LoginSerializer  # Import custom serializers for registration and login
from rest_framework.authtoken.models import Token  # Import Token model for token authentication
from rest_framework.permissions import AllowAny  # Import permission class to allow any user

class RegisterView(generics.CreateAPIView):
    """
    View for user registration.
    Allows new users to create an account by providing a username, email, and password.
    """
    serializer_class = RegisterSerializer  # Specify the serializer to be used for validation and creation
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view

class LoginView(generics.GenericAPIView):
    """
    View for user login.
    Authenticates the user and provides a token for subsequent API requests.
    """
    serializer_class = LoginSerializer  # Specify the serializer for login
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user login.
        Validates the provided credentials and returns an authentication token.
        """
        # Get the serializer instance with the request data
        serializer = self.get_serializer(data=request.data)

        # Validate the serializer and raise an exception if validation fails
        serializer.is_valid(raise_exception=True)

        # Retrieve the authenticated user from the validated data
        user = serializer.validated_data

        # Get or create an authentication token for the user
        token, _ = Token.objects.get_or_create(user=user)

        # Return the token in the response
        return Response({'token': token.key})

class LogoutView(generics.GenericAPIView):
    """
    View for user logout.
    Deletes the user's authentication token to log them out.
    """
    def post(self, request):
        """
        Handle POST request for user logout.
        Deletes the token associated with the authenticated user.
        """
        # Delete the user's auth token to log them out
        request.user.auth_token.delete()

        # Return a 204 No Content response to indicate successful logout
        return Response(status=status.HTTP_204_NO_CONTENT)

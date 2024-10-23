from django.urls import path  # Import the path function to define URL patterns
from .views import RegisterView, LoginView, LogoutView  # Import the views for registration, login, and logout

urlpatterns = [
    # URL pattern for user registration
    path('register/', RegisterView.as_view(), name='register'),  # Maps to the RegisterView for handling user registration

    # URL pattern for user login
    path('login/', LoginView.as_view(), name='login'),  # Maps to the LoginView for handling user authentication

    # URL pattern for user logout
    path('logout/', LogoutView.as_view(), name='logout'),  # Maps to the LogoutView for logging out the user
]

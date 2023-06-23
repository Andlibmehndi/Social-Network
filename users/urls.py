from django.urls import path
from .views import greeting, signup, UserDetailsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Routes for User
urlpatterns = [
    path('signup/', signup),
    path('ping/', greeting),

    # Authenticated Routes
    path('details/', UserDetailsView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='Login'),
    path('login-refresh/', TokenRefreshView.as_view(), name='Refresh Token'),
]
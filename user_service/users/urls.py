from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserDetailAPIView,
    VerifyCredentialsAPIView
)

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<uuid:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/verify/', VerifyCredentialsAPIView.as_view(), name='verify'),
]
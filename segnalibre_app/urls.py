from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

prefix = 'v1/'

urlpatterns = [
    path(prefix + 'users/', views.UserList.as_view()),
    path(prefix + 'books/', views.BookList.as_view()),
    path(prefix +'books/<int:pk>/', views.BookDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path(prefix + 'auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(prefix + 'auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path(prefix + 'auth/verify', TokenVerifyView.as_view(), name='token_verify')
]
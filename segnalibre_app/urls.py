from django.urls import path, include
from . import views

prefix = 'v1/'

urlpatterns = [
    path(prefix + 'users/', views.UserList.as_view()),
    path(prefix + 'books/', views.BookList.as_view()),
    path(prefix +'books/<int:pk>/', views.BookDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]
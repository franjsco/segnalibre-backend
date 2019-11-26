from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^v1/auth/', include('djoser.urls')),
    url(r'^v1/auth/', include('djoser.urls.jwt')),
    path('v1/books/', views.BookList.as_view()),
    path('v1/books/<int:pk>/', views.BookDetail.as_view()),
    #path('api-auth/', include('rest_framework.urls')),
]
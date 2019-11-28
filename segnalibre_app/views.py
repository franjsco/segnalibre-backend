
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import filters, generics, permissions
from rest_framework.views import APIView
from .serializers import BookSerializer, UserSerializer
from .models import Book
from .permissions import isOwner

# Create your views here.
class UserList(generics.ListAPIView):
    #queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    #queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated, isOwner]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author']
    ordering = ['title']

    def get_queryset(self):
        queryset = Book.objects.filter(owner=self.request.user)
        show = self.request.query_params.get('show', None)

        if show == 'all':
            queryset = queryset.filter(status='completed') | queryset.filter(status='uncompleted')
        elif show == 'completed':
            queryset = queryset.filter(status='completed')
        else:
            queryset = queryset.filter(status='uncompleted')

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated, isOwner]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Book.objects.filter(pk=pk, owner=self.request.user)

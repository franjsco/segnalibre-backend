import django_filters.rest_framework
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer, BookmarkSerilizer, UserSerializer
from .models import Book, Bookmark
from .permissions import isOwner

# Create your views here.
class UserList(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookList(APIView):
    serializer_class = BookSerializer
    #queryset = Book.objects.all()
    #filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    #search_fields = ['title', 'author']
    #ordering_fields = ['pub_date', 'title', 'author']
    #ordering = ['title']
    permission_classes = [permissions.IsAuthenticated, isOwner]

    def get(self, request, format=None):
        books = Book.objects.filter(owner=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookDetail(APIView):
    #serializer_class = BookSerializer
    #queryset = Book.objects.all()
    #filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    #search_fields = ['title', 'author']
    #ordering_fields = ['pub_date', 'title', 'author']
    #ordering = ['title']
    permission_classes = [permissions.IsAuthenticated, isOwner]

    def get_object(self, pk, owner=None):
        try:
            return Book.objects.get(pk=pk, owner=owner)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk, request.user)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        book = self.get_object(pk, request.user)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        book = self.get_object(pk, request.user)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
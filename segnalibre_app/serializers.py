from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Bookmark

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'publisher',
            'pub_date',
            'pages',
            'position',
            'owner',
            'created',
            'updated'
        )

class UserSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'books']

class BookmarkSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = (
            'id',
            'position',
            'book',
            'owner',
            'created'
        )
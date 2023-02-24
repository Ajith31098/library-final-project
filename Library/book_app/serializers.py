from rest_framework import serializers
from book_app.models import Book, BookRequest, BookAllocation
from user_app.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BookRequestSerializer(serializers.ModelSerializer):

    book_id = BookSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = BookRequest
        fields = '__all__'


class BookRequestReturnSerializer(serializers.ModelSerializer):

    book_id = BookSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = BookAllocation
        fields = '__all__'

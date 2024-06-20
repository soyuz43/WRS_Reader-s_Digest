# WRS_Readersapi/serializers/book_serializer.py
from rest_framework import serializers
from ..models.book import Book  # Import Book model
from .category_serializer import CategorySerializer

class BookSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()
    categories = CategorySerializer(many=True)

    def get_is_owner(self, obj):
        # Check if the authenticated user is the owner
        return self.context['request'].user == obj.user

    class Meta:
        model = Book  # Assign Book model
        fields = ['id', 'title', 'author', 'isbn_number', 'cover_image', 'is_owner', 'categories']

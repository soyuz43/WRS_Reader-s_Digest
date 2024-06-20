# File: WRS_Readersapi/views/books.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import serializers
from WRS_Readersapi.models import Book
from ..serializers.category_serializer import CategorySerializer  # Adjust import path as per your project structure
from ..serializers.book_serializer import BookSerializer




class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, context={'request': request})
            return Response(serializer.data)

        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        title = request.data.get('title')
        author = request.data.get('author')
        isbn_number = request.data.get('isbn_number')
        cover_image = request.data.get('cover_image')

        book = Book.objects.create(
            user=request.user,
            title=title,
            author=author,
            cover_image=cover_image,
            isbn_number=isbn_number)

        category_ids = request.data.get('categories', [])
        book.categories.set(category_ids)

        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            self.check_object_permissions(request, book)

            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()

                category_ids = request.data.get('categories', [])
                book.categories.set(category_ids)

                return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
            self.check_object_permissions(request, book)
            book.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

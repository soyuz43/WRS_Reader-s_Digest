# File: WRS_Readersapi/views/categories.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from WRS_Readersapi.models import Category
from WRS_Readersapi.serializers.category_serializer import CategorySerializer  # Adjust import path as per your project structure

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving categories.
    """
    
    def list(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

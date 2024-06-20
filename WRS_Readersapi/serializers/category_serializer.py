# File: WRS_Readersapi/serializers/category_serializer.py
from rest_framework import serializers
from WRS_Readersapi.models import Category  # Adjust the import path as per your project structure

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

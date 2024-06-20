# File: WRS_Readersapi/views/__init__.py

from .categories import CategoryViewSet
from .users import UserViewSet
from .books import BookViewSet
from .reviews import ReviewViewSet
from ..serializers.category_serializer import CategorySerializer
from ..serializers.book_serializer import BookSerializer
from ..serializers.review_serializer import ReviewSerializer  # Import ReviewSerializer

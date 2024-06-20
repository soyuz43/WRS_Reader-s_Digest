from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from WRS_Readersapi.views import UserViewSet, CategoryViewSet  # Import CategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet, basename='category')  # Register CategoryViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),  # Ensure trailing slashes
    path('register', UserViewSet.as_view({'post': 'register_account'}), name='register'),  # Ensure trailing slashes
    path('admin', admin.site.urls),
]

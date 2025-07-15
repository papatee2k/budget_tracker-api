from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriesViewSet, TransactionsViewSet        
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, basename='categories')
router.register(r'transactions', TransactionsViewSet, basename='transactions')
# patterns for the API
urlpatterns = [
    path('', include(router.urls)),
]  
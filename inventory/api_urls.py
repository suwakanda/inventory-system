# inventory/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')

urlpatterns = [
    path('', include(router.urls)),  # /api/inventory/ path
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'inventory', views.InventoryViewSet, basename='inventory')

urlpatterns = [
    path('api/', include(router.urls)), # /api
    path('', views.inventory_list, name='inventory_list'),  # /inventory/
    path('<int:id>/', views.inventory_detail, name='inventory_detail'),  # /inventory/<id>/
]
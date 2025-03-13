from django.shortcuts import render
from rest_framework import viewsets
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.filters import SearchFilter 

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.select_related('supplier').all()
    serializer_class = InventorySerializer
    filter_backends = [SearchFilter]
    search_fields  = ['name']
    
def inventory_list(request):
    items = Inventory.objects.select_related('supplier').all()
    return render(request, 'inventory/list.html', {'items': items})

def inventory_detail(request, id):
    item = Inventory.objects.select_related('supplier').get(id=id)
    return render(request, 'inventory/detail.html', {'item': item})
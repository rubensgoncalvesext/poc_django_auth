from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from poc.permissions import Permission

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # permission_classes = [Permission]

    def get_queryset(self):
        return Product.objects.all()

    

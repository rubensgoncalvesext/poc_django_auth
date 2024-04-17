from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    

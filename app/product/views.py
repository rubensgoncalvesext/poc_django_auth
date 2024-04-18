from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from product.services import ProductService
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self, pk):
        queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=pk)

    def list(self, request):
        return self.serializer_class(self.get_queryset(), many=True)

    def create(self, request):
        data = self.serializer_class(data=request.data)
        product = ProductService.create(data=data)
        return self.serializer_class(product)

    def retrieve(self, request, pk=None):
        return self.serializer_class(self.get_object(pk))

    def update(self, request, pk=None):
        raise NotImplementedError

    def partial_update(self, request, pk=None):
        raise NotImplementedError

    def destroy(self, request, pk=None):
        raise NotImplementedError

    

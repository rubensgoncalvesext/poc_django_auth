from product.models import Product
from product.serializers import ProductSerializer
from poc.thread_local import request_data


class ProductService:

    @classmethod
    def create(cls, data: ProductSerializer, created_by_id: int) -> Product:
       data.is_valid(raise_exception=True)
       record = Product()
       record.name = data.validated_data['name']
       record.price = data.validated_data['price']
       record.created_by = request_data.user.id
       return record

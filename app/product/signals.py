from django.db.models.signals import post_save
from django.dispatch import receiver
from product.models import Product
from poc.thread_local import request_data


@receiver(post_save, sender=Product)
def product_post_save(sender, **kwargs):
    print("Hi I'm a post signal!!")
    # Que usuario fiz a request?
    user = request_data.user

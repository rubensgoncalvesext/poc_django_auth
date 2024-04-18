from django.db import models
from poc import settings

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    created_by = models.BigIntegerField(null=True, blank=False, verbose_name='Creation User', db_index=True)
    modified_by = models.BigIntegerField(null=True, blank=False, verbose_name='Modified User', db_index=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

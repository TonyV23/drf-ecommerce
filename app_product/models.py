from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=20, blank=True)
    is_digital = models.BooleanField(default=False)
    branch = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name

from pytest_factoryboy import register

from .factories import CategoryFactory
from app_product.models import Category

register(CategoryFactory, model_class=Category)

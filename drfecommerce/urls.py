from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_product import views

router = DefaultRouter()
router.register(r'categories', views.CategoryView)
router.register(r'brands', views.BrandView)
router.register(r'products', views.ProductView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

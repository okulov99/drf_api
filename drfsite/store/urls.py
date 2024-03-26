from django.urls import path
from .views import ProductsAPIView

urlpatterns = [
    path('api/v1/products_list/', ProductsAPIView.as_view())
]

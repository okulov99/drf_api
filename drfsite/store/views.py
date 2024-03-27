from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Products
from .permissions import IsAdminOrReadOnly
from .serializers import ProductsSerializer


class ProductsAPIPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    pagination_class = ProductsAPIPagination
    permission_classes = IsAdminOrReadOnly





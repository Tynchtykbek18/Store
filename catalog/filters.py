import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    size = django_filters.CharFilter(field_name='size')
    brand = django_filters.CharFilter(field_name='brand')
    type = django_filters.CharFilter(field_name='type')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'size', 'brand', 'type']

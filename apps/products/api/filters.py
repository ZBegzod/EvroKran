import django_filters as filters
from apps.products.models import *


class TransportFilter(filters.FilterSet):
    category = filters.ModelChoiceFilter(queryset=Category.objects.all(), field_name='category')

    ton__gt = filters.NumberFilter(field_name='ton', lookup_expr='gt')
    ton__lt = filters.NumberFilter(field_name='ton', lookup_expr='lt')

    arrow__gt = filters.NumberFilter(field_name='arrow_length', lookup_expr='gt')
    arrow__lt = filters.NumberFilter(field_name='arrow_length', lookup_expr='lt')

    class Meta:
        model = Transport
        fields = ['category']


class TypeFilter(filters.FilterSet):
    class Meta:
        model = Transport
        fields = ['type_transport']

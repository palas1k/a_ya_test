import django_filters
from django_filters import FilterSet

from catalog.models import Item, Parameter


class ItemFilterset(FilterSet):
    name_field = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    param_fields = django_filters.ModelChoiceFilter(queryset=Parameter.objects.all())

    class Meta:
        model = Item
        fields = [
            'name_field',
            'param_fields',
        ]

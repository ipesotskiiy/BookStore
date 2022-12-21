import django_filters
from django_filters import FilterSet, RangeFilter, BaseInFilter, CharFilter

from product.models import Book


class CharFilterInFilter(BaseInFilter, CharFilter):
    pass


class GenreAndPriceFilter(FilterSet):
    genre = CharFilterInFilter(field_name='genre__id', lookup_expr='in')
    price = RangeFilter()

    class Meta:
        model = Book
        fields = ['genre', 'price']

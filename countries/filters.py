# filters.py
from django_filters import FilterSet, CharFilter
from countries.models import Country

class CountryFilter(FilterSet):
    languages = CharFilter(field_name='languages__name', lookup_expr='icontains')

    class Meta:
        model = Country
        fields = ['languages']

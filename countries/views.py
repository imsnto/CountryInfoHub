from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CountrySerializer
from .filters import CountryFilter
from .models import Country

# Create your views here.
class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CountryFilter
    search_fields = ['common_name', 'official_name']

    @action(detail=True, methods=['get'], url_path='region')
    def same_region(self, request, pk=None):
        try:
            country = self.get_object()

            if not country.region:
                return Response({'Region not found': 'No region data available for this country'}, status=404)
            same_region_countries = Country.objects.filter(region=country.region)
            serializer = self.get_serializer(same_region_countries, many=True)
            return Response(serializer.data)
        except Country.DoesNotExist as e:
            return Response({'Country not found': str(e)}, status=404)

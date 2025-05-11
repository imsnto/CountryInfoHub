from django.http import Http404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated

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
    permission_classes = [IsAuthenticated]

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

class CountryListView(LoginRequiredMixin, ListView):
    template_name = 'country_list.html'
    context_object_name = 'countries'
    paginate_by = 10

    def get_queryset(self):
        queryset = Country.objects.all()
        query = self.request.GET.get('country_name', None)
        if query:
            queryset = queryset.filter(
                Q(common_name__icontains=query) | Q(official_name__icontains=query)
            )
        return queryset

class CountryDetailView(LoginRequiredMixin, DetailView):
    queryset = Country.objects.all()
    template_name = 'countries/country_detail.html'
    context_object_name = 'country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_country = self.object

        language = self.request.GET.get('language', None)
        clicked = self.request.GET.get('btn', None)

        if clicked:
            same_region_countries = Country.objects.filter(region=current_country.region)
            context['clicked'] = True
            if language:
                context['language'] = language.capitalize()
                same_region_countries = same_region_countries.filter(languages__name__iexact=language)
            context['same_region_countries'] = same_region_countries
        return context

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CountryViewSet, CountryListView, CountryDetailView

router = DefaultRouter()
router.register('countries', CountryViewSet, basename='country')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', CountryListView.as_view(), name="country-list"),
    path('<int:pk>/', CountryDetailView.as_view(), name="country-detail"),
]
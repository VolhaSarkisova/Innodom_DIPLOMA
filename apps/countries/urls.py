from django.urls import path
from apps.countries.views import (
    CountryList,
    country_detail,
    city_detail,
)

urlpatterns = [
    path('', CountryList.as_view(), name='countries'),
    path('country-detail/<int:pk>/', country_detail, name='country'),
    path('city-detail/<int:pk>/', city_detail, name='city'),
]
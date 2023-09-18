from django.urls import path
from apps.countries.views import (
    CountryList,
    # CountryDetail,
    CountryCreate,
    CountryUpdate,
    CountryDelete,
    country_detail,
    city_detail,
)

urlpatterns = [
    path('', CountryList.as_view(), name='countries'),
    # path('country-detail/<int:pk>/', CountryDetail.as_view(), name='country'),
    path('country-detail/<int:pk>/', country_detail, name='country'),
    path('country-create/', CountryCreate.as_view(), name='country_create'),
    path('country-update/<int:pk>/', CountryUpdate.as_view(), name='country_update'),
    path('country-delete/<int:pk>/', CountryDelete.as_view(), name='country_delete'),

    path('city-detail/<int:pk>/', city_detail, name='city'),
]
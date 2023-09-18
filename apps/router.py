from django.urls import path, include

urlpatterns = [
    path('', include('apps.countries.urls')),
    path('user/', include('apps.users.urls')),
    path('hotel/', include('apps.hotels.urls')),
]
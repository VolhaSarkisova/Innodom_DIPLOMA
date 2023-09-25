from django.urls import path, include

urlpatterns = [
    path('', include('apps.countries.urls')),
    path('user/', include('apps.users.urls')),
    path('hotel/', include('apps.hotels.urls')),
    path('reservation/', include('apps.reservations.urls')),
    path('review/', include('apps.reviews.urls')),
    path('api/', include('api.urls')),
]
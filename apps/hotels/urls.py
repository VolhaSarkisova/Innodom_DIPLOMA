from django.urls import path

from apps.hotels.views import hotel_detail, room_detail

urlpatterns = [
    path('hotel-detail/<int:pk>/', hotel_detail, name='hotel'),
    path('room-detail/<int:pk>/', room_detail, name='room'),
]
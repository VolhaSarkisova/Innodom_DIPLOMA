from django.urls import path

from api.views import (
    HotelsFreeListAPIView,
    RoomsFreeListAPIView,
    UserReservsListAPIView,
    UserAddReservationAPIView
)

urlpatterns = [
    path('free_hotels/', HotelsFreeListAPIView.as_view()),
    path('free_rooms/', RoomsFreeListAPIView.as_view()),
    path('user_reservations/', UserReservsListAPIView.as_view()),
    path('user_add_reservation/', UserAddReservationAPIView.as_view()),
]
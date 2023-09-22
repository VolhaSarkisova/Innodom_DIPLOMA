from django.urls import path

from apps.reservations.views import (
    # reservation_detail,
    user_reservations,
    delete_user_reservation,
    reservation_detail,
    reservation_info

)

urlpatterns = [
    path('<int:pk>/', reservation_detail, name='reservation'),
    path('user-reservations/', user_reservations, name='user_reservations'),
    path('reservation-delete/<int:pk>/', delete_user_reservation, name='reservation_delete'),
    path('<int:pk>/<url>/', reservation_detail, name='reservation_detail'),
    path('reservation_info/<int:pk>/<date_start>/<date_end>/<info>', reservation_info, name='reservation_info')

]
from datetime import datetime, date

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request

from api.serializers import HotelSerializer, RoomSerializer, ReservationSerializer
from apps.hotels.models import Room, Hotel
from apps.reservations.models import Reservation


class HotelsFreeListAPIView(APIView):
    # http://127.0.0.1:8010/api/free_hotels/?search-date-start=2023-09-22&search-date-end=2023-09-22
    def get(self, request: Request):
        reservations = Reservation.objects.all()
        rooms = Room.objects.all()
        hotels = Hotel.objects.all()

        search_date_start = self.request.query_params.get('search-date-start')
        search_date_end = self.request.query_params.get('search-date-end')

        if search_date_start and search_date_end:
            date_start = datetime.strptime(search_date_start, '%Y-%m-%d')
            date_end = datetime.strptime(str(search_date_end), '%Y-%m-%d')
            date_now = datetime.strptime(str(date.today()), '%Y-%m-%d')
            if date_now <= date_start <= date_end:
                reservations = reservations.filter(Q(date__range=(date_start, date_end)))
                rooms = rooms.exclude(id__in=[reservation.room.id for reservation in reservations])
                hotels = hotels.filter(id__in=[room.hotel.id for room in rooms])

        serializer = HotelSerializer(hotels, many=True)

        return Response(serializer.data)


class RoomsFreeListAPIView(APIView):
    # http://127.0.0.1:8010/api/free_rooms/?search-date-start=2023-10-22&search-date-end=2023-10-22&hotel=1
    def get(self, request: Request):
        reservations = Reservation.objects.all()
        rooms = Room.objects.all()

        hotel_id = self.request.query_params.get('hotel')
        search_date_start = self.request.query_params.get('search-date-start')
        search_date_end = self.request.query_params.get('search-date-end')

        if search_date_start and search_date_end and hotel_id:
            date_start = datetime.strptime(search_date_start, '%Y-%m-%d')
            date_end = datetime.strptime(str(search_date_end), '%Y-%m-%d')
            date_now = datetime.strptime(str(date.today()), '%Y-%m-%d')
            if date_now <= date_start <= date_end:
                reservations = reservations.filter(date__range=(date_start, date_end))
                rooms = rooms.exclude(id__in=[reservation.room.id for reservation in reservations])
                rooms = rooms.filter(hotel=hotel_id)

        if rooms:
            serializer = RoomSerializer(rooms, many=True)

        return Response(serializer.data)

class UserReservsListAPIView(APIView):
    # http://127.0.0.1:8010/api/user_reservations/
    def get(self, request: Request):
        # http://127.0.0.1:8010/api/user_reservations/?user=1
        # user = self.request.query_params.get('user')
        # reservations = Reservation.objects.filter(Q(user=user))

        user = self.request.user.id
        reservations = Reservation.objects.filter(user=user)

        serializer = ReservationSerializer(reservations, many=True)

        return Response(serializer.data)

class UserAddReservationAPIView(APIView):
    # http://127.0.0.1:8010/api/user_add_reservation/
    def post(self, request: Request):
        serializer = ReservationSerializer(data=request.data)

        if serializer.is_valid():
            reservations = Reservation.objects.filter(date=request.data.get('date'))
            rooms = Room.objects.exclude(id__in=[reservation.room.id for reservation in reservations])

            if request.data.get('room') in [room.id for room in rooms]:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




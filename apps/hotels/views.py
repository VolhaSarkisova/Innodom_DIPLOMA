from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from apps.hotels.models import (
    Hotel,
    Room,
    HotelPhotos,
    RoomPhotos
)
from apps.reservations.models import Reservation

# @login_required
def hotel_detail(request, pk):
    search_room = request.GET.get('search-area') or ''
    search_date_start = request.GET.get('search-date-start') or ''
    search_date_end = request.GET.get('search-date-end') or ''

    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = ''
    hotel_photos = HotelPhotos.objects.filter(hotel=pk)[0:1]
    reservations = ''

    context = {
        'hotel': hotel,
        'rooms': rooms,
        'hotel_photos': hotel_photos,
        'reservations': reservations
    }

    if search_date_start != '' and search_date_end != '':
        date_start = datetime.strptime(search_date_start, '%Y-%m-%d')
        date_end = datetime.strptime(str(search_date_end), '%Y-%m-%d')
        date_now = datetime.strptime(str(date.today()), '%Y-%m-%d')
        if date_now <= date_start <= date_end:
            context['rooms'] = Room.objects.filter(hotel=pk)
            if search_room:
                context['rooms'] = context['rooms'].filter(
                    number_of_seats__icontains=search_room
                )
            context['reservations'] = Reservation.objects.filter(
                date__range=(date_start, date_end))
            context['rooms'] = context['rooms'].exclude(
                id__in=[reservation.room.id for reservation in context['reservations']])
    return render(request, 'hotels/hotel_detail.html', context)

# @login_required
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    room_photos = RoomPhotos.objects.filter(room=pk)

    context = {
        'room': room,
        'room_photos': room_photos
    }

    return render(request, 'hotels/room_detail.html', context)

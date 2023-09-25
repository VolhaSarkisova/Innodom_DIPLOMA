from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404
from apps.hotels.models import Room, Hotel
from apps.reservations.forms import ReservationCreateForm
from apps.reservations.models import Reservation

@login_required()
def user_reservations(request):
    search_date_start = request.GET.get('search-date-start') or ''
    search_date_end = request.GET.get('search-date-end') or ''

    if request.user.is_superuser:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)

    if search_date_start != '' and search_date_end != '':
        date_start = datetime.strptime(search_date_start, '%Y-%m-%d')
        date_end = datetime.strptime(str(search_date_end), '%Y-%m-%d')
        if date_start <= date_end:
            reservations = Reservation.objects.filter(date__range=(date_start, date_end))

    rooms = Room.objects.filter(id__in=[reservation.room.id for reservation in reservations])
    hotels = Hotel.objects.filter(id__in=[room.hotel.id for room in rooms])

    context = {
        'reservations': reservations,
        'hotels': hotels,
    }
    return render(request, "reservations/user_reservations.html", context)

@login_required()
def delete_user_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    reservation.delete()

    return redirect("user_reservations")

@login_required()
def reservation_detail(request, pk, url):
    date_start = datetime.strptime(url[(url.index('search-date-start')+len('search-date-start')+1):
                                       (url.index('search-date-start')+len('search-date-start')+1+10)], '%Y-%m-%d').date()
    date_end = datetime.strptime(url[(url.index('search-date-end')+len('search-date-end')+1):
                                     (url.index('search-date-end')+len('search-date-end')+1+10)], '%Y-%m-%d').date()

    reserved = Reservation.objects.filter(date__range=(date_start, date_end))
    flag = True
    for item in reserved:

        if item.room.id == pk:
            flag = False
            break

    if flag:
        date = date_start
        while date <= date_end:
            form = ReservationCreateForm()
            reservation = form.save(commit=False)
            reservation.room_id = pk
            reservation.user_id = request.user.id
            reservation.date = date
            date += timedelta(days=1)
            reservation.save()
        return redirect("reservation_info", pk, date_start, date_end, 'successfully')
    else:
        return redirect("reservation_info", pk, date_start, date_end, 'booking error')

@login_required()
def reservation_info(request, pk, date_start, date_end, info):
    room = Room.objects.filter(pk=pk)

    context = {
        'info': info,
        'date_start': date_start,
        'date_end': date_end,
        'room': room
    }

    return render(request, "reservations/reservation_info.html", context)







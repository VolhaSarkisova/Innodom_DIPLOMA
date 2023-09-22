import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from apps.hotels.models import Room
from apps.reservations.forms import ReservationCreateForm
from apps.reservations.models import Reservation


# @login_required()
# def reservation_detail(request, pk):
#     room = Room.objects.filter(pk=pk)
#     print(request.GET.get('params'))
#     if request.method == "POST":
#         form = ReservationCreateForm(request.POST, request.FILES)
#         reservation = form.save(commit=False)
#         reservation.room_id = pk
#         reservation.user_id = request.user.id
#
#         if form.is_valid():
#             reservation.save()
#             if request.user.is_superuser:
#                 return redirect("countries")
#             else:
#                 return redirect("user_reservations")
#     else:
#         form = ReservationCreateForm()
#
#     context = {
#         'form': form,
#         'room': room
#     }
#
#     return render(request, "reservations/reservation_form.html", context)

@login_required()
def user_reservations(request):
    if request.user.is_superuser:
        reservations = Reservation.objects.all()
    else:
        reservations = Reservation.objects.filter(user=request.user)

    context = {
        'reservations': reservations,
    }

    return render(request, "reservations/user_reservations.html", context)

@login_required()
def delete_user_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)

    reservation.delete()

    return redirect("user_reservations")

@login_required()
def reservation_detail(request, pk, url):

    date_start = datetime.datetime.strptime(url[(url.index('search-date-start')+len('search-date-start')+1):(url.index('search-date-start')+len('search-date-start')+1+10)], '%Y-%m-%d').date()
    date_end = datetime.datetime.strptime(url[(url.index('search-date-end')+len('search-date-end')+1):(url.index('search-date-end')+len('search-date-end')+1+10)], '%Y-%m-%d').date()
    print(date_start, date_end)
    reserved = Reservation.objects.filter(date__range=(date_start, date_end))
    flag = True
    for item in reserved:
        print(item.room)
        if item.room.id == pk:
            flag = False
            print(flag)
            break

    if flag:
        date = date_start
        while date <= date_end:
            form = ReservationCreateForm()
            reservation = form.save(commit=False)
            reservation.room_id = pk
            reservation.user_id = request.user.id
            reservation.date = date
            date += datetime.timedelta(days=1)
            reservation.save()
        return redirect("reservation_info", pk, date_start, date_end, 'успешно')
        # redirect("user_reservations")
    else:
        return redirect("reservation_info", pk, date_start, date_end, 'запрещено. Повторное бронирование номера невозможно.')

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







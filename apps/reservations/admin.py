from django.contrib import admin
from apps.reservations.models import Reservation

@admin.register(Reservation)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('room', 'date', 'reserved', 'user', 'comment')
    list_filter = ('room', 'date', 'user')

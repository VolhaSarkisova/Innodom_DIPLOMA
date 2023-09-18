from django.contrib import admin
from apps.hotels.models import Hotel, HotelPhotos, Room, RoomPhotos

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'number_of_stars')
    search_fields = ('name', )
    list_filter = ('name', 'city', 'number_of_stars')

@admin.register(HotelPhotos)
class HotelPhotosAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'photo')
    list_filter = ('hotel', )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'number', 'category', 'number_of_seats', 'price', 'currency')
    search_fields = ('number_of_seats', )
    list_filter = ('hotel', 'number', 'category', 'number_of_seats')

@admin.register(RoomPhotos)
class RoomPhotosAdmin(admin.ModelAdmin):
    list_display = ('room', 'photo')
    list_filter = ('room', )
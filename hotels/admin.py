from django.contrib import admin

from hotels.models import Hotel, HotelPhotos, Room, RoomPhotos


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'number_of_stars')
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(HotelPhotos)
class HotelPhotosAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'photo')
    search_fields = ('hotel', )
    list_filter = ('hotel', )

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'number', 'category', 'number_of_seats', 'price', 'currency')
    search_fields = ('hotel', )
    list_filter = ('hotel', )

@admin.register(RoomPhotos)
class RoomPhotosAdmin(admin.ModelAdmin):
    list_display = ('room', 'photo')
    search_fields = ('room', )
    list_filter = ('room', )
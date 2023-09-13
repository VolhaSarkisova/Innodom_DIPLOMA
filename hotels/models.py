from django.db import models

from countries.models import City, Currency

NUMBER_OF_STARS = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)
ROOM_CATEGORY = (
    ('Standard room', 'Standard room'),
    ('Improved room', 'Improved room'),
    ('Family room', 'Family room'),
    ('Apartments', 'Apartments'),
    ('Suite room', 'Suite room'),
    ('Deluxe room', 'Deluxe room'),
    ('Presidential suite', 'Presidential suite'),
)
NUMBER_OF_SEATS = (
    ('single room', 'single room'),
    ('double room', 'double room'),
    ('triple room', 'triple room'),
    ('quadruple room', 'quadruple room'),
    ('five-bed room', 'five-bed room'),
    ('six-bed room', 'six-bed room')
)
class Hotel(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Hotel name",
                            help_text="Enter a hotel name")
    city = models.ForeignKey(City,
                             on_delete=models.PROTECT,
                             related_name='hotel_city')
    address = models.CharField(max_length=256,
                               verbose_name="Hotel address",
                               help_text="Enter a hotel address")
    number_of_stars = models.IntegerField(verbose_name="Number of stars",
                                          help_text="Enter a number of stars",
                                          choices=NUMBER_OF_STARS,
                                          default=3)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hotels'
        ordering = ['city', 'name']

class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name="hotel_photos_hotel")
    photo = models.ImageField(upload_to='hotel_photos',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.hotel

    class Meta:
        verbose_name_plural = 'Photos of hotels'
        ordering = ['hotel']

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name="room_hotel")
    number = models.CharField(max_length=4,
                              verbose_name='Room number',
                              help_text='Enter a room number')
    category = models.CharField(max_length=20,
                                choices=ROOM_CATEGORY,
                                default='Standard room',
                                verbose_name='Room category',
                                help_text='Enter a room category')
    number_of_seats = models.CharField(max_length=15,
                                       choices=NUMBER_OF_SEATS,
                                       default='single room')
    price = models.DecimalField(max_digits=15,
                                decimal_places=2)
    currency = models.ForeignKey(Currency,
                                 on_delete=models.PROTECT,
                                 related_name='room_currency')

    def __str__(self):
        return f'{self.hotel}: {self.number}'

    class Meta:
        verbose_name_plural = 'Rooms'
        ordering = ['hotel', 'number']

class RoomPhotos(models.Model):
    room = models.ForeignKey(Room,
                             on_delete=models.CASCADE,
                             related_name='room_photos_room')
    photo = models.ImageField(upload_to='room_photos',
                              blank=True,
                              null=True)
    def __str__(self):
        return self.room

    class Meta:
        verbose_name_plural = 'Photos of rooms'
        ordering = ['room']
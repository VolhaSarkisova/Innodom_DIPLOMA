from django.contrib.auth.models import User
from django.db import models

from hotels.models import Room


class Reservation(models.Model):
    room = models.ForeignKey(Room,
                             on_delete=models.PROTECT,
                             related_name='reservation_room')
    date = models.DateTimeField(blank=False,
                                null=False)
    reserved = models.BooleanField(default=True)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             related_name='reservation_user')
    comment = models.TextField(max_length=2000,
                               verbose_name='Booking comment',
                               help_text='Enter a booking comment')

    def __str__(self):
        return f'The {self.user} has booked a {self.room} for a {self.date}'

    class Meta:
        verbose_name_plural = 'Reservations'
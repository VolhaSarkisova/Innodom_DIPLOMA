from django.contrib.auth.models import User
from django.db import models

from apps.hotels.models import Room


class Reservation(models.Model):
    room = models.ForeignKey(Room,
                             on_delete=models.PROTECT,
                             related_name='reservation_room')
    date = models.DateField(blank=False,
                            null=False)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT,
                             related_name='reservation_user')
    comment = models.TextField(max_length=2000,
                               verbose_name='Booking comment',
                               help_text='Enter a booking comment',
                               null=True,
                               blank=True)

    def __str__(self):
        return f'The {self.user} has booked a {self.room} for a {self.date}'

    class Meta:
        verbose_name_plural = 'Reservations'
        ordering = ['-date']
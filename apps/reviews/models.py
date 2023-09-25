from django.contrib.auth.models import User
from django.db import models

from apps.hotels.models import Hotel

GRADE = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Review(models.Model):
    hotel = models.ForeignKey(Hotel,
                              on_delete=models.CASCADE,
                              related_name='review_hotel')
    grade = models.IntegerField(choices=GRADE,
                                default=5)
    comment = models.TextField(max_length=3000,
                               verbose_name='Сomment',
                               help_text='Enter a comment')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='review_user')
    created_at = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField(default=False)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='replies')
    def __str__(self):
        return f'User:{self.user} | Grade: {self.grade} | DateTime: {self.created_at}'
    class Meta:
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']

    @property
    def children(self):
        return Review.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
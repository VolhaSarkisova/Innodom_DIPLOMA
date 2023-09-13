from django.db import models

from countries.models import City

NUMBER_OF_STARS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
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
                                          default='3')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Hotels'
        ordering = ['city', 'name']
from django.db import models

class Country(models.Model):
    # United Kingdom of Great Britain and Northern Ireland
    name = models.CharField(max_length=58,
                            verbose_name="Country name",
                            help_text="Enter a country name")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

class City(models.Model):
    # Bangkok's full name is the longest
    name = models.CharField(max_length=168,
                            verbose_name="Сity name",
                            help_text="Enter a city name")
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT,
                                related_name='city_country')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['name']
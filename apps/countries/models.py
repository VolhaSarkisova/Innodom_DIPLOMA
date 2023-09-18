from django.db import models

class Country(models.Model):
    # United Kingdom of Great Britain and Northern Ireland
    name = models.CharField(max_length=58,
                            verbose_name="Country name",
                            help_text="Enter a country name")
    description = models.TextField(max_length=3000,
                                   verbose_name="Country description",
                                   help_text="Enter a country description",
                                   null=True,
                                   blank=True)
    main_photo = models.ImageField(upload_to='country_photos',
                              blank=True,
                              null=True)
    attractions = models.TextField(max_length=3000,
                                   verbose_name="Country attractions",
                                   help_text="Enter a country attractions",
                                   null=True,
                                   blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ['name']

class CountryPhotos(models.Model):
    country = models.ForeignKey(Country,
                              on_delete=models.CASCADE,
                              related_name="country_photos_country")
    photo = models.ImageField(upload_to='country_photos',
                              blank=True,
                              null=True)
    def __str__(self):
        return f'Country: {self.country} Photo: {self.photo}'
    class Meta:
        verbose_name_plural = 'Photos of countries'
        ordering = ['country']

class City(models.Model):
    # Bangkok's full name is the longest
    name = models.CharField(max_length=168,
                            verbose_name="Сity name",
                            help_text="Enter a city name")
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT,
                                related_name='city_country')
    description = models.TextField(max_length=3000,
                                   verbose_name="City description",
                                   help_text="Enter a ciry description",
                                   null=True,
                                   blank=True)
    main_photo = models.ImageField(upload_to='city_photos',
                              blank=True,
                              null=True)
    attractions = models.TextField(max_length=3000,
                                   verbose_name="City attractions",
                                   help_text="Enter a city attractions",
                                   null=True,
                                   blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['name']

class CityPhotos(models.Model):
    city = models.ForeignKey(City,
                              on_delete=models.CASCADE,
                              related_name="city_photos_city")
    photo = models.ImageField(upload_to='city_photos',
                              blank=True,
                              null=True)
    def __str__(self):
        return f'City: {self.city} Photo: {self.photo}'
    class Meta:
        verbose_name_plural = 'Photos of cities'
        ordering = ['city']

class Currency(models.Model):
    country = models.ForeignKey(Country,
                                on_delete=models.PROTECT,
                                related_name='currency_country')
    name = models.CharField(max_length=5,
                            verbose_name="Currency name",
                            help_text="Enter a currency name")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['name']
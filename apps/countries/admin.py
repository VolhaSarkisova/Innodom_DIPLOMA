from django.contrib import admin
from apps.countries.models import Country, City, Currency, CountryPhotos, CityPhotos


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country', 'name')
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(CountryPhotos)
class CountryPhotosAdmin(admin.ModelAdmin):
    list_display = ('country', 'photo')
    list_filter = ('country', )

@admin.register(CityPhotos)
class CityHotelPhotosAdmin(admin.ModelAdmin):
    list_display = ('city', 'photo')
    list_filter = ('city', )
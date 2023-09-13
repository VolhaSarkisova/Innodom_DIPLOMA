from django.contrib import admin

from countries.models import Country, City, Currency


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
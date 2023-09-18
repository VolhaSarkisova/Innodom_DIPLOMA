from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from rest_framework.generics import get_object_or_404

from apps.countries.models import Country, City, CountryPhotos, CityPhotos
from apps.hotels.models import Hotel

class CountryList(LoginRequiredMixin, ListView):
    model = Country
    context_object_name = 'countries'
    template_name = "countries/country_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['countries'] = context['countries'].filter(
        #     user=self.request.user
        # ).count()
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['countries'] = context['countries'].filter(
                name__icontains=search_input
            )
        context['search-input'] = search_input
        return context

# class CountryDetail(LoginRequiredMixin, DetailView):
#     model = Country
#     context_object_name = 'country'
def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    cities = City.objects.filter(country=pk)
    country_photos = CountryPhotos.objects.filter(country=pk)[0:3]

    context = {
        'country': country,
        'cities': cities,
        'country_photos': country_photos
    }

    search_city = request.GET.get('search-area') or ''
    if search_city:
        context['cities'] = context['cities'].filter(
            name__icontains=search_city
        )

    return render(request, 'countries/country_detail.html', context)

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    hotels = Hotel.objects.filter(city=pk)
    city_photos = CityPhotos.objects.filter(city=pk)

    context = {
        'city': city,
        'hotels': hotels,
        'city_photos': city_photos
    }


    search_hotel = request.GET.get('search-area') or ''
    if search_hotel:
        context['hotels'] = context['hotels'].filter(
            name__icontains=search_hotel
        )

    return render(request, 'countries/city_detail.html', context)

class CountryCreate(LoginRequiredMixin, CreateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    template_name = "countries/country_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CountryCreate, self).form_valid(form)

class CountryUpdate(LoginRequiredMixin, UpdateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    template_name = "countries/country_form.html"

class CountryDelete(LoginRequiredMixin, DeleteView):
    model = Country
    template_name = 'countries/country_delete.html'
    success_url = reverse_lazy('countries')

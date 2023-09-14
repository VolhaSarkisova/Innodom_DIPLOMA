from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from apps.countries.models import Country

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

class CountryDetail(LoginRequiredMixin, DetailView):
    model = Country
    context_object_name = 'country'

class CountryCreate(LoginRequiredMixin, CreateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('countries')
    template_name = "countries/country_form.html"

    def form_valid(self, form):
        # form.instance.user = self.request.user
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

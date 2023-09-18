from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from apps.reservations.models import Reservation


# class ReservationProcess(LoginRequiredMixin, ListView):
#     model = Reservation
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         search_


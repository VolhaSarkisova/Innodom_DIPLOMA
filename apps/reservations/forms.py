from django import forms
from .models import Reservation

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('room', 'date', 'user', 'comment',)

        widgets = {
            "room": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "date": forms.DateInput(attrs={
                "class": INPUT_CLASSES,
            }),
            "user": forms.Select(attrs={
                "class": INPUT_CLASSES,
            }),
            "comment": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            }),
        }
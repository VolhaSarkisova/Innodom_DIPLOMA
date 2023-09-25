from django import forms
from .models import Review

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['grade', 'comment']

        widgets = {
            "grade": forms.NumberInput({
                "class": INPUT_CLASSES,
                "min": 1,
                "max": 5
            }
            ),
            "comment": forms.TextInput(attrs={
                "class": INPUT_CLASSES,
            })
        }

class ModerationForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['moderation']

    widgets = {
        "moderation": forms.NullBooleanSelect()
    }
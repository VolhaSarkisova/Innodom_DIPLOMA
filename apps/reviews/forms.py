from django import forms
from .models import Review

INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"

class ReviewForm(forms.ModelForm):
    # def __init__(self, hotel_id, username, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['hotel'].queryset = Hotel.objects.filter(pk=hotel_id)
    #     self.fields['user'].queryset = User.objects.filter(username=username)
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
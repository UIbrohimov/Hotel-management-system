from django import forms
from tempus_dominus.widgets import DatePicker

from .models import Reservation


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['room', 'date_from', 'date_to', 'adults', 'children']

        widgets = {
            'date_from': DatePicker(attrs={'placeholder': '... sanadan'}),
            'date_to': DatePicker(attrs={'placeholder': '... sanagacha'}),
        }

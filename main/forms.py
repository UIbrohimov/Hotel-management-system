from django import forms
from tempus_dominus.widgets import DatePicker

from main.models import Region
from .models import *


class ReservationForm(forms.Form):
    address = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Qayerga bormoqchisiz ...'
    )
    start_date = forms.DateField(widget=DatePicker(
        attrs={'placeholder': 'Boshlanish sanasi'},
    ))
    end_date = forms.DateField(widget=DatePicker(
        attrs={'placeholder': 'Tugash sanasi'},
    ))

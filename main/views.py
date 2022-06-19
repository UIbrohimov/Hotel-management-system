from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, ListView, CreateView
from django.db.models import Q

from reservations.models import Reservation

from .models import Room
from .forms import ReservationForm


class IndexView(View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'pages/home.html', {'form': form})

    def post(self, request):
        print("post worked", request.POST)
        form = ReservationForm(request.POST)
        rooms = None
        if form.is_valid():
            address = form.cleaned_data['address']
            address = address.get_descendants(include_self=True)
            start_date = form.cleaned_data.get('start_date', None)
            end_date = form.cleaned_data.get('end_date', None)

            request.session["start_date"] = str(start_date)
            request.session["end_date"] = str(end_date)

            reservs = Reservation.objects.filter(
                Q(date_from__lte=start_date) & Q(date_to__lte=start_date)
                | Q(date_from__gte=end_date)).distinct().values_list("room__id", flat=True)

            rooms = Room.objects.filter(
                (Q(id__in=reservs) | Q(reservations__isnull=True)) & Q(hotel__address__in=address)
            ).distinct()

        return render(request, 'pages/home.html', {'form': form, 'search_results': rooms})


home = IndexView.as_view()

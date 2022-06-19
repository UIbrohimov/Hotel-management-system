from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import CreateView, DetailView, ListView

from main.models import Room
from .forms import ReservationForm
from .models import Reservation


class MakeReservation(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/make_reservation.html'

    def get_room(self, *args, **kwargs):
        room_id = self.kwargs.get('room_id', None)
        return Room.objects.filter(id=room_id).first()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["room"] = self.get_room()
        return ctx

    def get_initial(self):
        initial = super().get_initial()
        initial.update({
            'room': self.get_room(),
            'date_from': self.request.session.get('start_date', None),
            'date_to': self.request.session.get('end_date', None)
            })
        return initial

    def form_valid(self, form):
        reservation = form.save(commit=False)
        reservation.room = self.get_room()
        reservation.person = self.request.user
        reservation.save()
        return redirect('reservations:list')


make_reservation = MakeReservation.as_view()


class ReservationList(ListView):
    model = Reservation
    template_name = 'reservations/reservation_list.html'

    def get_queryset(self):
        return self.model.objects.filter(person=self.request.user)


reservation_list = ReservationList.as_view()

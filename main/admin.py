from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(GuestHouse)
class GuestHouseadmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'active']
    search_fields = ['name', 'code']
    list_filter = ['active']
    list_per_page = 10
    list_display_links = ['name']
    list_editable = ['active']


@admin.register(Rooms)
class Roomsadmin(admin.ModelAdmin):
    list_display = ['roomID', 'room_type', 'guesthouse', 'price', 'services']
    search_fields = ['roomID', 'room_type', 'guesthouse', 'price', 'services']
    list_filter = ['room_type', 'guesthouse']
    list_per_page = 10
    list_display_links = ['roomID']


@admin.register(Reservation)
class Reservationadmin(admin.ModelAdmin):
    list_display = ['bookingID', 'start_date', 'end_date', 'user_booked', 'rooms_allocated', 'guesthouse', 'status', 'waiting']
    search_fields = ['bookingID', 'start_date', 'end_date', 'user_booked', 'rooms_allocated', 'guesthouse', 'status', 'waiting']
    list_filter = ['status', 'waiting']
    list_per_page = 10
    list_display_links = ['bookingID']
    list_editable = ['status', 'waiting']


@admin.register(PreReservation)
class PreReservationadmin(admin.ModelAdmin):
    list_display = ['room_type', 'start_date', 'end_date', 'guesthouse']
    search_fields = ['start_date', 'end_date', 'guesthouse', 'room_type']
    list_filter = ['guesthouse']
    list_per_page = 10
    list_display_links = ['start_date']
    list_editable = ['guesthouse']


@admin.register(Payment)
class Paymentadmin(admin.ModelAdmin):
    list_display = ['paymentID', 'amount', 'reservation', 'user_booked', 'payment_time']
    search_fields = ['paymentID', 'amount', 'reservation', 'user_booked', 'payment_time']
    list_per_page = 10
    list_display_links = ['paymentID']
    list_editable = ['amount']


@admin.register(Refund)
class Refundadmin(admin.ModelAdmin):
    list_display = ['refundID', 'amount', 'payment', 'user_booked', 'reservation', 'refund_time']
    search_fields = ['refundID', 'amount', 'payment', 'user_booked', 'reservation', 'refund_time']
    list_filter = ['payment', 'reservation']
    list_per_page = 10
    list_display_links = ['refundID']
    list_editable = ['amount']


@admin.register(GuestDetails)
class GuestDetailsadmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'reservation']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'reservation']
    list_filter = ['reservation']
    list_per_page = 10
    list_display_links = ['first_name']


@admin.register(Feedback)
class Feedbackadmin(admin.ModelAdmin):
    list_display = ['feedbackID', 'user_of', 'time', 'feed']
    search_fields = ['feedbackID', 'user_of', 'time', 'feed']
    list_per_page = 10
    list_display_links = ['feedbackID']


@admin.register(WaitingOn)
class WaitingOnadmin(admin.ModelAdmin):
    list_display = ['resID', 'date_booked', 'start_date', 'end_date']
    search_fields = ['resID', 'date_booked', 'start_date', 'end_date']
    list_filter = ['resID']
    list_per_page = 10
    list_display_links = ['resID']

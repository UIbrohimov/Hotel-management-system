from django.urls import path


from .views import make_reservation, reservation_list, reservation_detail

urlpatterns = [
    path('make-reservation/<int:room_id>', make_reservation, name='make_reservation'),
    path('reservation-list/', reservation_list, name='list'),
    path('reservation-detail/<int:pk>/', reservation_detail, name="detail")
]
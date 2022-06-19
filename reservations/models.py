from datetime import datetime
from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    room = models.ForeignKey(
        'main.Room',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='reservations'
    )
    person = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True)
    date_from = models.DateField("Дата заезда")
    date_to = models.DateField("Дата выезда")
    adults = models.PositiveSmallIntegerField("Взрослые", default=1)
    children = models.PositiveSmallIntegerField("Дети", default=0)
    created = models.DateTimeField("Создано", default=timezone.now)
    payed = models.BooleanField("Оплачено", default=False)

    def __str__(self) -> str:
        return f"{self.room.hotel} - {self.room}, From {self.date_from}  -  to {self.date_to}"

    def get_price(self) -> int:
        return self.room.price * (self.date_to - self.date_from).days

    def get_total_price(self) -> int:
        return self.get_price() * (self.adults + self.children)

    @property
    def status(self):
        if timezone.now().today().date() < self.date_from:
            return "Boshlanmagan"
        elif timezone.now().today().date() < self.date_to:
            return "Faol"
        else:
            return "Tugallangan"

    class Meta:
        verbose_name = "rezervatsiya"
        verbose_name_plural = "Rezervatsiyalar"

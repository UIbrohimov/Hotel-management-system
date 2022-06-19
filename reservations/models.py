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
    created = models.DateTimeField("Создано", default=timezone.now)
    payed = models.BooleanField("Оплачено", default=False)

    def __str__(self) -> str:
        return f"{self.room}, From {self.date_from} to {self.date_to}"

    class Meta:
        verbose_name = "rezervatsiya"
        verbose_name_plural = "Rezervatsiyalar"

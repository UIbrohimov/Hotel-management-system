from django.db import models
from django.utils import timezone


class Payment(models.Model):
    reservation = models.OneToOneField(
        'reservations.Reservation',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='payments'
    )
    amount = models.IntegerField("Сумма", default=0)
    created = models.DateTimeField("Создано", default=timezone.now)
    completed = models.BooleanField("Оплачено", default=False)

    def __str__(self) -> str:
        return f"{self.reservation}, {self.amount}"

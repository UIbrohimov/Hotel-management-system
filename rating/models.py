from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from main.models import Room
# Create your models here.

class Rating(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='rates'
    )
    rate = models.IntegerField("Оценка", default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    person = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="rates"
    )
    contact = models.CharField("Контакный номер", max_length=13, blank=True)
    comment = models.TextField("Отзыв", blank=True)
    published = models.BooleanField("Публиковано", default=False)
    created = models.DateTimeField("Создано", default=timezone.now)

    class Meta:
        verbose_name = _("reyting")
        verbose_name_plural = _("Reytinglar")

    def __str__(self) -> str:
        return f"# {self.pk} - {self.rate}"

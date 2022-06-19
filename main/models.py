from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Region(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = 'hudud'
        verbose_name_plural = 'Hududlar'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='hotels'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mehmonxona'
        verbose_name_plural = 'Mehmonxonalar'


class Rating(models.Model):
    product = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='ratings'
    )
    rate = models.IntegerField("Оценка", default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField("Отзыв", blank=True)
    created = models.DateTimeField("Создано", default=timezone.now)

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Mehmonxonalar baholari"

    def __str__(self) -> str:
        return "# " + str(self.pk)


class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField("Описание", blank=True)
    created = models.DateTimeField("Создано", default=timezone.now)

    class Meta:
        verbose_name = "Xona turi"
        verbose_name_plural = "Xona turlari"

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='rooms'
    )
    room_type = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='rooms'
    )
    name = models.CharField(max_length=100)
    price = models.IntegerField("Цена", default=0)
    description = models.TextField("Описание", blank=True)
    created = models.DateTimeField("Создано", default=timezone.now)

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"

    def __str__(self):
        return self.name


class RoomRating(models.Model):
    product = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='ratings'
    )
    rate = models.IntegerField("Оценка", default=0, validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField("Отзыв", blank=True)
    created = models.DateTimeField("Создано", default=timezone.now)

    class Meta:
        verbose_name = "baho"
        verbose_name_plural = "Xonalar baholari"

    def __str__(self) -> str:
        return "# " + str(self.pk)


from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    phone = models.CharField("Телефон", max_length=20, blank=True)
    address = models.CharField("Адрес", max_length=100, blank=True)
    passport_image = models.ImageField("Паспорт", upload_to='passport', blank=True)

    class Meta:
        verbose_name = "malumot"
        verbose_name_plural = "Foydalanuvchi malumotlari"

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

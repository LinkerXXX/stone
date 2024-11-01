from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    registration_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(
        verbose_name="Фотография пользователя",
        blank=True,
        upload_to=settings.MEDIA_USER_IMAGE_DIR,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

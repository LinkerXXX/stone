from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from user.models import User

User = get_user_model()


class Note(models.Model):
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} + {self.user}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

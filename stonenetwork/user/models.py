from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password

class User(models.Model):

    nick = models.CharField(max_length=50, verbose_name = "Логин", help_text = "Логин пользователя", blank = True)
    first_name = models.CharField(max_length=50, verbose_name = "Имя", help_text = "Имя пользователя", blank = True)
    last_name = models.CharField(max_length=50, verbose_name = "Фамилия", help_text = "Фамилия пользователя", blank = True)
    registration_date = models.DateTimeField(auto_now_add = True)
    email = models.EmailField(max_length=50, unique = True, blank = False)
    avatar = models.ImageField(verbose_name = "Фотография пользователя", blank = True, upload_to=settings.MEDIA_USER_IMAGE_DIR,)

    USERNAME_FIELD = 'nick'  # Поле для аутентификации
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # Поля, которые требуются при создании пользователя

    def __str__(self):
        return f'{self.id}'
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    

from django.db import models



class User(models.Model):

    nick = models.CharField(max_length=50, verbose_name = "Логин", help_text = "Логин пользователя", blank = True)
    first_name = models.CharField(max_length=50, verbose_name = "Имя", help_text = "Имя пользователя", blank = True)
    last_name = models.CharField(max_length=50, verbose_name = "Фамилия", help_text = "Фамилия пользователя", blank = True)
    registration_date = models.DateTimeField(auto_now_add = True)
    email = models.EmailField(max_length=50, unique = True, blank = False)
    identify = models.SlugField(max_length=20)

    class Meta:
        
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.identify}'
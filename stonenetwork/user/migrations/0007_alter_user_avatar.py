# Generated by Django 5.1.2 on 2024-10-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Фотография пользователя'),
        ),
    ]

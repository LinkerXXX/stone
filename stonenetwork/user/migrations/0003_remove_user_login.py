# Generated by Django 5.1.2 on 2024-10-21 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options_alter_user_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
    ]

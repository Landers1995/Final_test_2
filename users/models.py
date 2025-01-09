from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_email

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="E-mail", validators=[validate_email])
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', **NULLABLE)
    date_born = models.DateField(verbose_name='Дата рождения')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи о пользователе')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения записи о пользователе')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"

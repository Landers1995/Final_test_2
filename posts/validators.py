from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
from datetime import date


def validate_date_of_birth(self, value):
    # Проверка возраста (должен быть 18 лет)
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise serializers.ValidationError("Вы должны быть не моложе 18 лет.")
    return value


def validate_username(self, value):
    # Проверка на запрещённые слова в логине
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    if any(word in value.lower() for word in forbidden_words):
        raise serializers.ValidationError("Логин не должен содержать запрещенные слова.")
    return value

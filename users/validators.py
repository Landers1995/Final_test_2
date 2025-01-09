from django.core.exceptions import ValidationError
import re


def validate_password(value):
    if len(value) < 8:
        raise ValidationError('Пароль должен содержать не менее 8 символов.')
    if not re.search(r'\d', value):
        raise ValidationError('Пароль должен содержать хотя бы одну цифру.')


def validate_email(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    if not any(value.endswith('@' + domain) for domain in allowed_domains):
        raise ValidationError('Разрешены домены: mail.ru, yandex.ru.')

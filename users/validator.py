import re
from django.core.exceptions import ValidationError
from django.conf import Settings, settings


def validate_password(field):
    pattern = re.compile(r'^[A-Za-z0-9]+$')
    language = settings.LANGUAGE_CODE
    error_messages = [
        {
            'ru-ru':'Пароль должен содержать только латинские буквы и цифры',
            'en-us': 'Must contain A-Z a-z letters and 0-9 numbers'
        },
        {
            'ru-ru': 'Пароль должен содержать от 8 до 16 символов',
            'en-us': 'Password length must be between 8 and 16 charters'
        }
    ]
    try:
        if not bool(re.match(pattern, field)):
            print(error_messages[0][language])
            raise ValidationError(error_messages[0][language])
        if not 8 <= len(field) <= 16:
            print(error_messages[1][language])
            raise ValidationError(error_messages[1][language])
    except KeyError:
        print('Не знаю такого языка!!!')
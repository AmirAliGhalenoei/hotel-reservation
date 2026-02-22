from django.core.exceptions import ValidationError
import re



def validate_iranian_phone(value):
    pattern = r'^(09\d{9}|0\d{2}\d{7})$'
    if not re.match(pattern, value):
        raise ValidationError(
            f'{value} شماره تلفن معتبر نیست.'
        )
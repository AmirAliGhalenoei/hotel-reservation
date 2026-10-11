from django.core.exceptions import ValidationError


def national_code_validator(national_code):
    if len(national_code) != 10:
        raise ValidationError("کد ملی نامعتبر")
    return national_code

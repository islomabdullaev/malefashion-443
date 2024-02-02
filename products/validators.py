from django.core.exceptions import ValidationError


def rating_value_validate(value):
    if not (1 <= value <= 5):
        raise ValidationError(
            ("Value must be between 1 and 5 !"),
            params={"value": value},
        )
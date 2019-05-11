from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

phone_regex = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message=_('Phone number is not valid'),
)

from django.conf import settings
from django.utils.translation import gettext_lazy as _

POSTAL_ADDRESS_L10N = getattr(settings, "POSTAL_ADDRESS_L10N", True)

# each address line is a tuple of format (field_label, required)
POSTAL_ADDRESS_LINE1 = getattr(settings, "POSTAL_ADDRESS_LINE1", (_("Street"), False))
POSTAL_ADDRESS_LINE2 = getattr(settings, "POSTAL_ADDRESS_LINE2", (_("Area"), False))
POSTAL_ADDRESS_CITY = getattr(settings, "POSTAL_ADDRESS_CITY", (_("City"), False))
POSTAL_ADDRESS_STATE = getattr(settings, "POSTAL_ADDRESS_STATE", (_("State"), False))
POSTAL_ADDRESS_CODE = getattr(settings, "POSTAL_ADDRESS_CODE", (_("Zip code"), False))

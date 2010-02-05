from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# each address line is a tuple of format (field_label, required)
POSTAL_ADDRESS_FIRSTNAME = getattr(settings, "POSTAL_ADDRESS_FIRSTNAME", (_(u"First name"), True))
POSTAL_ADDRESS_LASTNAME = getattr(settings, "POSTAL_ADDRESS_LASTNAME", (_(u"Last name"), True))
POSTAL_ADDRESS_LINE1 = getattr(settings, "POSTAL_ADDRESS_LINE1", (_(u"Company name"), False))
POSTAL_ADDRESS_LINE2 = getattr(settings, "POSTAL_ADDRESS_LINE2", (_(u"Street"), False))
POSTAL_ADDRESS_LINE3 = getattr(settings, "POSTAL_ADDRESS_LINE3", (_(u"City"), False))
POSTAL_ADDRESS_LINE4 = getattr(settings, "POSTAL_ADDRESS_LINE4", (_(u"State"), False))
POSTAL_ADDRESS_LINE5 = getattr(settings, "POSTAL_ADDRESS_LINE5", (_(u"Zip code"), False))
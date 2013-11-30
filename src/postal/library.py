from django import forms
from postal import settings as postal_settings
from postal.forms import PostalAddressForm
from postal.forms.ar.forms import ARPostalAddressForm
from postal.forms.co.forms import COPostalAddressForm
from postal.forms.cz.forms import CZPostalAddressForm
from postal.forms.de.forms import DEPostalAddressForm
from postal.forms.gb.forms import GBPostalAddressForm
from postal.forms.ie.forms import IEPostalAddressForm
from postal.forms.mx.forms import MXPostalAddressForm
from postal.forms.nl.forms import NLPostalAddressForm
from postal.forms.pl.forms import PLPostalAddressForm
from postal.forms.ru.forms import RUPostalAddressForm
from postal.forms.us.forms import USPostalAddressForm

# TODO: Auto-import these forms
country_map = {
    "co": COPostalAddressForm,
    "cz": CZPostalAddressForm,
    "de": DEPostalAddressForm,
    "gb": GBPostalAddressForm,
    "ie": IEPostalAddressForm,
    "mx": MXPostalAddressForm,
    "nl": NLPostalAddressForm,
    "pl": PLPostalAddressForm,
    "ru": RUPostalAddressForm,
    "us": USPostalAddressForm,
    "ar": ARPostalAddressForm,
}


def form_factory(country_code=None):
    if country_code is not None:
        if postal_settings.POSTAL_ADDRESS_L10N:
            return country_map.get(country_code.lower(), PostalAddressForm)

    return PostalAddressForm

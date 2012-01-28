from django import forms
from postal import settings as postal_settings
from postal.forms import PostalAddressForm
from postal.forms.de.forms import DEPostalAddressForm
from postal.forms.gb.forms import GBPostalAddressForm
from postal.forms.ie.forms import IEPostalAddressForm
from postal.forms.nl.forms import NLPostalAddressForm
from postal.forms.us.forms import USPostalAddressForm
from postal.forms.cz.forms import CZPostalAddressForm
from postal.forms.pl.forms import PLPostalAddressForm

# TODO: Auto-import these forms
country_map = {
    "cz": CZPostalAddressForm,
    "de": DEPostalAddressForm,
    "gb": GBPostalAddressForm,
    "ie": IEPostalAddressForm,
    "nl": NLPostalAddressForm,
    "pl": PLPostalAddressForm,
    "us": USPostalAddressForm,
}

def form_factory(country_code=None):
    if country_code is not None:    
        if postal_settings.POSTAL_ADDRESS_L10N:
            return country_map.get(country_code.lower(), PostalAddressForm)

    return PostalAddressForm

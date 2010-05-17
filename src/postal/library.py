# django imports
from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.forms import PostalAddressForm

from de.forms import DEPostalAddressForm
from gb.forms import GBPostalAddressForm
from ie.forms import IEPostalAddressForm
from nl.forms import NLPostalAddressForm
from us.forms import USPostalAddressForm
import settings as postal_settings


country_map = {"de": DEPostalAddressForm,
               "gb": GBPostalAddressForm,
               "ie": IEPostalAddressForm,
               "nl": NLPostalAddressForm,
               "us": USPostalAddressForm,
              }

def get_postal_form_class(country_code):
    if postal_settings.POSTAL_ADDRESS_L10N:
        return country_map.get(country_code.lower(), PostalAddressForm)
    else:
        return PostalAddressForm

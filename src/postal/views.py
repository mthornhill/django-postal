from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.forms import PostalAddressForm
from postal.library import country_map

def get_postal_form_class(country_code):
    return country_map.get(country_code, PostalAddressForm)



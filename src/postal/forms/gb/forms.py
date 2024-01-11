""" from http://www.bitboost.com/ref/international-address-formats.html#Great-Britain"""
from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.gb.forms import GBPostcodeField, GBCountySelect

from postal.forms import PostalAddressForm


class GBPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    line2 = forms.CharField(label=_("Area"), required=False, max_length=100)
    city = forms.CharField(label=_("Town"), max_length=100)
    state = forms.CharField(label=_("County"), widget=GBCountySelect, max_length=100)
    code = GBPostcodeField(label=_("Postcode"))

    def __init__(self, *args, **kwargs):
        super(GBPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "GB"

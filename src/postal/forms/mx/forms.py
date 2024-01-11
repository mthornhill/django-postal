""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.mx.forms import MXStateSelect, MXZipCodeField

from postal.forms import PostalAddressForm


class MXPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    line2 = forms.CharField(label=_("Number"), max_length=100)
    city = forms.CharField(label=_("City"), max_length=100)
    state = forms.CharField(label=_("State"), widget=MXStateSelect)
    code = MXZipCodeField(label=_("Zip Code"))

    def __init__(self, *args, **kwargs):
        super(MXPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "MX"

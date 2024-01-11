""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from postal.forms import PostalAddressForm


class USPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=50)
    line2 = forms.CharField(label=_("Area"), required=False, max_length=100)
    city = forms.CharField(label=_("City"), max_length=50)
    state = USStateField(label=_("US State"), widget=USStateSelect)
    code = USZipCodeField(label=_("Zip Code"))

    def __init__(self, *args, **kwargs):
        super(USPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "US"

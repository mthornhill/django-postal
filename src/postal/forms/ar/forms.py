""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.ar.forms import ARProvinceSelect, ARPostalCodeField

from postal.forms import PostalAddressForm


class ARPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=50)
    line2 = forms.CharField(label=_("Number"), max_length=50)
    city = forms.CharField(label=_("City"), max_length=50)
    state = forms.CharField(label=_("Province"), widget=ARProvinceSelect)
    code = ARPostalCodeField(label=_("Zip Code"))

    def __init__(self, *args, **kwargs):
        super(ARPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "AR"

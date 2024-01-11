from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.cz.forms import CZPostalCodeField

from postal.forms import PostalAddressForm


class CZPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    city = forms.CharField(label=_("City"), max_length=100)
    code = CZPostalCodeField(label=_("Zip Code"))

    def __init__(self, *args, **kwargs):
        super(CZPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop("line2")
        self.fields.pop("state")
        self.fields["country"].initial = "CZ"

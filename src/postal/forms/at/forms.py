from collections import OrderedDict

from django import forms
from django.utils.translation import gettext_lazy as _

from localflavor.at.forms import ATZipCodeField

from postal.forms import PostalAddressForm


class ATPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    city = forms.CharField(label=_("City"), max_length=100)
    code = ATZipCodeField(label=_("Zip Code"))

    def __init__(self, *args, **kwargs):
        super(ATPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop("line2")
        self.fields.pop("state")
        self.fields["country"].initial = "AT"
        self.fields = OrderedDict((k, self.fields[k]) for k in ["line1", "code", "city", "country"])

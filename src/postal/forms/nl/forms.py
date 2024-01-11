from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.nl.forms import NLZipCodeField

from postal.forms import PostalAddressForm


class NLPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), required=False, max_length=100)
    line2 = forms.CharField(label=_("Area"), required=False, max_length=100)
    city = forms.CharField(label=_("Town/City"), required=False, max_length=100)
    code = NLZipCodeField(label=_("Zip Code"))

    class Meta:
        exclude = ("state",)

    def __init__(self, *args, **kwargs):
        super(NLPostalAddressForm, self).__init__(*args, **kwargs)
        # we have to manually pop the inherited line5
        self.fields.pop("state")
        self.fields["country"].initial = "NL"

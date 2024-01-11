from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.pl.forms import PLPostalCodeField

from postal.forms import PostalAddressForm


class PLPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    city = forms.CharField(label=_("City"), max_length=100)
    code = PLPostalCodeField(label=_("Zip code"))

    def __init__(self, *args, **kwargs):
        super(PLPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop("line2")
        self.fields.pop("state")
        self.fields["country"].initial = "PL"

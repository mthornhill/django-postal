from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.ru.forms import RUCountySelect, RURegionSelect, RUPostalCodeField, RUPostalCodeField

from postal.forms import PostalAddressForm


class RUPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    line2 = forms.CharField(label=_("Area"), required=False, max_length=100, widget=RURegionSelect)
    city = forms.CharField(label=_("City"), max_length=100)
    state = forms.CharField(label=_("County"), required=False, max_length=100, widget=RUCountySelect)
    code = RUPostalCodeField(label=_("Postal code"), required=False)

    def __init__(self, *args, **kwargs):
        super(RUPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "RU"

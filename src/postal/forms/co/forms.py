""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import gettext_lazy as _
from localflavor.co.forms import CODepartmentSelect

from postal.forms import PostalAddressForm


class COPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_("Street"), max_length=100)
    line2 = forms.CharField(label=_("Number"), max_length=100)
    state = forms.CharField(label=_("Department"), max_length=50, widget=CODepartmentSelect)

    def __init__(self, *args, **kwargs):
        super(COPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields["country"].initial = "CO"
        self.fields["code"].initial = "000000"
        self.fields["code"].widget = forms.HiddenInput()

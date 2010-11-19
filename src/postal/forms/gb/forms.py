""" from http://www.bitboost.com/ref/international-address-formats.html#Great-Britain"""
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.uk.forms import UKPostcodeField, UKCountySelect

from postal.forms import PostalAddressForm

class GBPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=100)
    line2 = forms.CharField(label=_(u"Area"), required=False, max_length=100)
    city = forms.CharField(label=_(u"Town"), max_length=100)
    state = forms.CharField(label=_(u"County"), widget=UKCountySelect, max_length=100)
    code = UKPostcodeField(label=_(u"Postcode"))

    def __init__(self, *args, **kwargs):
        super(GBPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].initial = "GB"
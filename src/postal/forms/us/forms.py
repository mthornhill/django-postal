""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from postal.forms import PostalAddressForm

class USPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=50)
    line2 = forms.CharField(label=_(u"Area"), required=False, max_length=100)
    city = forms.CharField(label=_(u"City"), max_length=50)
    state = USStateField(label=_(u"US State"), widget=USStateSelect)
    code = USZipCodeField(label=_(u"Zip Code"))

    def __init__(self, *args, **kwargs):
        super(USPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].initial = "US"

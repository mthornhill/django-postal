""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.forms import USStateField, USStateSelect, USZipCodeField

from postal.forms import PostalAddressForm

class USPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Company name"), required=False, max_length=50)
    line2 = forms.CharField(label=_(u"Street"), max_length=100)
    line3 = USZipCodeField(label=_(u"Zip Code"))
    line4 = forms.CharField(label=_(u"City"), max_length=50)
    line5 = USStateField(label=_(u"US State"), widget=USStateSelect)

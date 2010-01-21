""" from http://www.bitboost.com/ref/international-address-formats.html#Great-Britain"""
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.de.forms import DEZipCodeField, DEStateSelect

from postal.forms import PostalAddressForm

class DEPostalAddressForm(PostalAddressForm):    
    line1 = forms.CharField(label=_(u"Company name"), required=False, max_length=50)
    line2 = forms.CharField(label=_(u"Street"), max_length=100)
    line3 = DEZipCodeField(label=_(u"Zip Code"))
    line4 = forms.CharField(label=_(u"City"), max_length=50)
    line5 = forms.CharField(label=_(u"State"), widget=DEStateSelect)

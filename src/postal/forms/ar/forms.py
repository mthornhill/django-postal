""" http://www.bitboost.com/ref/international-address-formats.html """
from django import forms
from django.utils.translation import ugettext_lazy as _
from localflavor.ar.forms import ARProvinceSelect, ARPostalCodeField

from postal.forms import PostalAddressForm

class ARPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=50)
    line2 = forms.CharField(label=_(u"Number"), max_length=50)
    city = forms.CharField(label=_(u"City"), max_length=50)
    state = forms.CharField(label=_(u"Province"), widget=ARProvinceSelect)
    code = ARPostalCodeField(label=_(u"Zip Code"))

    def __init__(self, *args, **kwargs):
        super(ARPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields['country'].initial = "AR"

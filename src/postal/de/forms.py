from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.de.forms import DEZipCodeField

from postal.forms import PostalAddressForm

class DEPostalAddressForm(PostalAddressForm):    
    line1 = forms.CharField(label=_(u"Company name"), required=False, max_length=100)
    line2 = forms.CharField(label=_(u"Street"), required=False, max_length=100)
    city = forms.CharField(label=_(u"City"), required=False, max_length=100)
    code = DEZipCodeField(label=_(u"Zip Code"))

    def __init__(self, *args, **kwargs):
        super(DEPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop('state')
        self.fields['country'].initial = "DE"

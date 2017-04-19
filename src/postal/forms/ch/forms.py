from django import forms
from django.utils.translation import ugettext_lazy as _

from localflavor.ch.forms import CHZipCodeField

from postal.forms import PostalAddressForm


class CHPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=100)
    city = forms.CharField(label=_(u"City"), max_length=100)
    code = CHZipCodeField(label=_(u"Zip Code"))

    def __init__(self, *args, **kwargs):
        super(CHPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop('line2')
        self.fields.pop('state')
        self.fields['country'].initial = "CH"
        self.fields = OrderedDict((k, self.fields[k]) for k in ['line1', 'code', 'city', 'country'])

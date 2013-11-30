""" from http://homepages.iol.ie/~discover/mail.htm"""
from django import forms
from django.utils.translation import ugettext_lazy as _
from postal.forms import PostalAddressForm
from localflavor.ie.forms import IECountySelect


class IEPostalAddressForm(PostalAddressForm):
    line1 = forms.CharField(label=_(u"Street"), max_length=100)
    line2 = forms.CharField(label=_(u"Area"), max_length=100, required=False)
    city = forms.CharField(label=_(u"Town/City"), max_length=100)
    state = forms.CharField(label=_(u"County"), widget=IECountySelect(), max_length=100)

    class Meta:
        exclude = ('code',)

    def __init__(self, *args, **kwargs):
        super(IEPostalAddressForm, self).__init__(*args, **kwargs)
        self.fields.pop('code')
        self.fields['country'].initial = "IE"

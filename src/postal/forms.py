from django import forms
from django.utils.translation import ugettext_lazy as _

from models import PostalAddress
from settings import POSTAL_ADDRESS_LINE1, POSTAL_ADDRESS_LINE2, POSTAL_ADDRESS_CITY, POSTAL_ADDRESS_STATE, POSTAL_ADDRESS_CODE

class PostalAddressForm(forms.ModelForm):
    line1 = forms.CharField(label=POSTAL_ADDRESS_LINE1[0], required=POSTAL_ADDRESS_LINE1[1], max_length=100)
    line2 = forms.CharField(label=POSTAL_ADDRESS_LINE2[0], required=POSTAL_ADDRESS_LINE2[1], max_length=100)
    city = forms.CharField(label=POSTAL_ADDRESS_CITY[0], required=POSTAL_ADDRESS_CITY[1], max_length=100)
    state = forms.CharField(label=POSTAL_ADDRESS_STATE[0], required=POSTAL_ADDRESS_STATE[1], max_length=100)
    code = forms.CharField(label=POSTAL_ADDRESS_CODE[0], required=POSTAL_ADDRESS_CODE[1], max_length=100)

    class Meta:
        model = PostalAddress
        
    def __unicode__(self):
        return self.line1 + ', ' + self.line2 + ', ' + self.city + ', ' + self.state + ', ' + self.code + ', ' + self.country

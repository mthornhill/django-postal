from django import forms
from django.utils.translation import ugettext_lazy as _

from models import PostalAddress
from settings import POSTAL_ADDRESS_FIRSTNAME, POSTAL_ADDRESS_LASTNAME, POSTAL_ADDRESS_LINE1, POSTAL_ADDRESS_LINE2, POSTAL_ADDRESS_LINE3, POSTAL_ADDRESS_LINE4, POSTAL_ADDRESS_LINE5

class PostalAddressForm(forms.ModelForm):
    line1 = forms.CharField(label=POSTAL_ADDRESS_LINE1[0], required=POSTAL_ADDRESS_LINE1[1], max_length=100)
    line2 = forms.CharField(label=POSTAL_ADDRESS_LINE2[0], required=POSTAL_ADDRESS_LINE2[1], max_length=100)
    line3 = forms.CharField(label=POSTAL_ADDRESS_LINE3[0], required=POSTAL_ADDRESS_LINE3[1], max_length=100)
    line4 = forms.CharField(label=POSTAL_ADDRESS_LINE4[0], required=POSTAL_ADDRESS_LINE4[1], max_length=100)
    line5 = forms.CharField(label=POSTAL_ADDRESS_LINE5[0], required=POSTAL_ADDRESS_LINE5[1], max_length=100)

    class Meta:
        model = PostalAddress
        exclude = ['location',]
        
    def __unicode__(self):
        return self.line1 + ', ' + self.line2 + ', ' + self.line3 + self.line4 + ', ', + self.line5 + ', ' + self.country

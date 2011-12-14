from django import forms
from django.utils.translation import ugettext_lazy as _
from django_countries import countries

from postal.settings import POSTAL_ADDRESS_LINE1, POSTAL_ADDRESS_LINE2, POSTAL_ADDRESS_CITY, POSTAL_ADDRESS_STATE, POSTAL_ADDRESS_CODE

country_list = (('', '-'*45),) + countries.COUNTRIES
country_dict = {}
for (key, value) in countries.COUNTRIES: country_dict[key] = value

class PostalAddressForm(forms.Form):
    line1 = forms.CharField(label=POSTAL_ADDRESS_LINE1[0], required=POSTAL_ADDRESS_LINE1[1], max_length=100)
    line2 = forms.CharField(label=POSTAL_ADDRESS_LINE2[0], required=POSTAL_ADDRESS_LINE2[1], max_length=100)
    city = forms.CharField(label=POSTAL_ADDRESS_CITY[0], required=POSTAL_ADDRESS_CITY[1], max_length=100)
    state = forms.CharField(label=POSTAL_ADDRESS_STATE[0], required=POSTAL_ADDRESS_STATE[1], max_length=100)
    code = forms.CharField(label=POSTAL_ADDRESS_CODE[0], required=POSTAL_ADDRESS_CODE[1], max_length=100)
    country = forms.ChoiceField(label=_(u"Country"), choices=country_list)

    def clean_country(self):
        data = self.cleaned_data['country']
        if data not in country_dict.keys():
            raise forms.ValidationError("You must select a country")
        return data

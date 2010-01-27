from ie.forms import IEPostalAddressForm
from de.forms import DEPostalAddressForm
from gb.forms import GBPostalAddressForm
from us.forms import USPostalAddressForm


country_map = {"de": DEPostalAddressForm, 
               "ie": IEPostalAddressForm,
               "gb": GBPostalAddressForm,
               "us": USPostalAddressForm,
              }


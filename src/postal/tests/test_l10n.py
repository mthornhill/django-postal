from django.test import TestCase
from django.utils.translation import ugettext

from postal.library import form_factory
import postal.settings
import postal.forms


class PostalTests(TestCase):
    def test_environment(self):
        """Just make sure everything is set up correctly."""
        self.assert_(True)
        
        
    def test_get_de_address(self):
        """
        Tests that we get the correct widget for Germny
        """
        german_form_class = form_factory("de")
        self.assertNotEqual(german_form_class, None)
        
        # only use required fields
        test_data = {'code': '12345',}
        form = german_form_class(data=test_data)
        
        self.assertEqual(form.fields['line1'].label.lower(), "street")
        self.assertEqual(form.fields.has_key('line2'), False)
        self.assertEqual(form.fields['city'].label.lower(), "city")
        self.assertEqual(form.fields['code'].label.lower(), "zip code")
        
    def test_get_ie_address(self):
        """
        Tests that we get the correct widget for Ireland
        """
        irish_form_class = form_factory("ie")
        self.assertNotEqual(irish_form_class, None)

        # only use required fields
        test_data = {'line1': 'street', 'city': 'Tullamore',
                     'state': 'offaly',  }
        form = irish_form_class(data=test_data)
        
        self.assertEqual(form.fields['line1'].label.lower(), "street")
        self.assertEqual(form.fields['line2'].label.lower(), "area")
        self.assertEqual(form.fields['city'].label.lower(), "town/city")
        self.assertEqual(form.fields['state'].label.lower(), "county")
        
    def test_incorrect_country_code(self):
        """
        Tests that we don't throw an exception for an incorrect country code
        """
        no_country_form_class = form_factory("xx")
        self.assertNotEqual(no_country_form_class, None)
        
        form = no_country_form_class()
        
        self.assertEqual(form.fields['line1'].label.lower(), "street")
        self.assertEqual(form.fields['line2'].label.lower(), "area")
        self.assertEqual(form.fields['city'].label.lower(), "city")
        self.assertEqual(form.fields['state'].label.lower(), "state")
        self.assertEqual(form.fields['code'].label.lower(), "zip code")

    def test_set_default_address(self):
        # change line1 label and make it required
        postal.settings.POSTAL_ADDRESS_LINE1 = ('Crazy address label', True)
        # we have to reload the postal form for the setting above to take effect
        reload(postal.forms)
        form = postal.forms.PostalAddressForm(data={})
        self.assertEqual('Crazy address label' in form.as_p(), True)
        self.assertEqual('Company name' in form.as_p(), False)

        # create a blank form
        form = postal.forms.PostalAddressForm(data={})

        # Our form is invalid as line1 is now required
        self.assertEqual(form.is_valid(), False)

        form = postal.forms.PostalAddressForm(data={'line1': 'my street', 'country': 'DE'})
        self.assertEqual(form.is_valid(), True)
        
    def test_4_line_address(self):
        netherlands_form_class = form_factory("nl")
        self.assertNotEqual(netherlands_form_class, None)
        test_data = {'code': '1234AB'}
        form = netherlands_form_class(data=test_data)
        self.assertEqual(form.fields['line1'].label.lower(), "street")
        self.assertEqual(form.fields['line2'].label.lower(), "area")
        self.assertEqual(form.fields['city'].label.lower(), "town/city")
        self.assertEqual(form.fields.get('state'), None)
        self.assertEqual(form.fields['code'].label.lower(), "zip code")
        
    def test_no_localisation(self):
        postal.settings.POSTAL_ADDRESS_L10N = False
        postal.settings.POSTAL_ADDRESS_LINE1 = ('a', False)
        postal.settings.POSTAL_ADDRESS_LINE2 = ('b', False)
        postal.settings.POSTAL_ADDRESS_CITY = ('c', False)
        postal.settings.POSTAL_ADDRESS_STATE = ('d', False)
        postal.settings.POSTAL_ADDRESS_CODE = ('e', False)
        reload(postal.forms)
        reload(postal.library)

        noloc_form_class = form_factory("nl")
        self.assertNotEqual(noloc_form_class, None)
        test_data = {'code': '1234AB'}
        form = noloc_form_class(data=test_data)
        
        self.assertEqual(form.fields['line1'].label, "a")
        self.assertEqual(form.fields['line2'].label, "b")
        self.assertEqual(form.fields['city'].label, "c")
        self.assertEqual(form.fields['state'].label, 'd')
        self.assertEqual(form.fields['code'].label, "e")
        
        
        
        
        

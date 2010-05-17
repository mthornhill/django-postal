from django.test import TestCase
from django.utils.translation import ugettext

from postal.library import get_postal_form_class
from postal.models import PostalAddress
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
        self.assertEqual(PostalAddress.objects.count(), 0)
        german_form_class = get_postal_form_class("de")
        self.assertNotEqual(german_form_class, None)
        
        # only use required fields
        test_data = {'code': '12345',}
        form = german_form_class(data=test_data)
        
        self.assertEqual(form.fields['line1'].label, "Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['city'].label, "City")
        self.assertEqual(form.fields['code'].label, "Zip Code")
        form.save()
        self.assertEqual(PostalAddress.objects.count(), 1)
    
    def test_get_ie_address(self):
        """
        Tests that we get the correct widget for Ireland
        """
        self.assertEqual(PostalAddress.objects.count(), 0)
        irish_form_class = get_postal_form_class("ie")
        self.assertNotEqual(irish_form_class, None)

        # only use required fields
        test_data = {'line1': 'street', 'city': 'Tullamore',
                     'state': 'offaly',  }
        form = irish_form_class(data=test_data)
        
        self.assertEqual(form.fields['line1'].label, "Street")
        self.assertEqual(form.fields['line2'].label, "Area")
        self.assertEqual(form.fields['city'].label, "Town/City")
        self.assertEqual(form.fields['state'].label, "County")
        form.save()
        self.assertEqual(PostalAddress.objects.count(), 1)
    
    def test_incorrect_country_code(self):
        """
        Tests that we don't throw an exception for an incorrect country code
        """
        no_country_form_class = get_postal_form_class("xx")
        self.assertNotEqual(no_country_form_class, None)
        
        form = no_country_form_class()
        
        self.assertEqual(form.fields['line1'].label, "Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['city'].label, "City")
        self.assertEqual(form.fields['state'].label, "State")
        self.assertEqual(form.fields['code'].label, "Zip code")

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

        self.assertEqual(PostalAddress.objects.count(), 0)
        form = postal.forms.PostalAddressForm(data={'line1': 'blah'})
        self.assertEqual(form.is_valid(), True)
        form.save()
        self.assertEqual(PostalAddress.objects.count(), 1)
        
    def test_4_line_address(self):
        self.assertEqual(PostalAddress.objects.count(), 0)
        netherlands_form_class = get_postal_form_class("nl")
        self.assertNotEqual(netherlands_form_class, None)
        test_data = {'code': '1234AB'}
        form = netherlands_form_class(data=test_data)
        self.assertEqual(form.fields['line1'].label, "Company name")
        self.assertEqual(form.fields['line2'].label, "Street")
        self.assertEqual(form.fields['city'].label, "Town/City")
        self.assertEqual(form.fields.get('state'), None)
        self.assertEqual(form.fields['code'].label, "Zip Code")
        form.save()
        self.assertEqual(PostalAddress.objects.count(), 1)

        
        
        
        
        
        

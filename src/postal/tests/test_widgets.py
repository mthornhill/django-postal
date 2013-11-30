from django.test import TestCase
from django.utils.translation import ugettext
from django import forms
from postal.library import form_factory
from postal import settings as postal_settings


class PostalWidgetsTests(TestCase):
    def test_environment(self):
        """Just make sure everything is set up correctly."""
        self.assert_(True)

    def test_ar_widgets(self):
        """
        Tests that we get the correct widget for Argentina
        """
        # enable L10N
        postal_settings.POSTAL_ADDRESS_L10N = True

        form_class = form_factory("ar")
        self.assertNotEqual(form_class, None)

        # only use required fields
        test_data = {
            'line1': 'Maipu',
            'line2': '270',
            'city': 'Ciudad de Buenos Aires',
            'state': 'B',
            'code': 'C1006ACT',
        }
        form = form_class(data=test_data)

        from localflavor.ar.forms import ARProvinceSelect, ARPostalCodeField
        self.assertIsInstance(form.fields['state'].widget, ARProvinceSelect)
        self.assertIsInstance(form.fields['code'], ARPostalCodeField)
        self.assertEqual(form.fields['country'].initial, 'AR')

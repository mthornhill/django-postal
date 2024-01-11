django-postal
=============

(Based upon http://github.com/mthornhill/django-postal)

.. WARNING::
   This project is in ALPHA mode and the API is in flux.

A django application that provides a location agnostic model for postal addresses.

The motivation behind this project is that most countries have different forms of
postal addresses e.g. http://www.bitboost.com/ref/international-address-formats.html ,
http://en.wikipedia.org/wiki/Address_%28geography%29

This app assumes that all postal addresses worldwide can be made up of 5 optional
address lines plus a country code.

It then localizes the title of each line dependant on the country selected.
Further information on each address line can be gleaned from
``django.contrib.localflavor`` fields and widgets e.g. for the UK ::

    from django import forms
    from django.utils.translation import gettext_lazy as _
    from django.contrib.localflavor.uk.forms import UKPostcodeField, UKCountySelect

    from postal.forms import PostalAddressForm

    class GBPostalAddressForm(PostalAddressForm):
        line1 = forms.CharField(label=_(u"Street"), required=False, max_length=50)
        line2 = forms.CharField(label=_(u"Area"), max_length=50)
        city = forms.CharField(label=_(u"Town"), max_length=50)
        state = forms.CharField(label=_(u"County"), widget=UKCountySelect, max_length=50)
        code = UKPostcodeField(label=_(u"Postcode"))

It is hoped that various contributors will contribute address formats per country
and that eventually this address information could find it's way back in to
django.contrib.localflavor


Dependencies
============

django-countries (http://pypi.python.org/pypi/django-countries)

Usage
=====

1. Add django-countries and django-postal to your ``INSTALLED_APPS`` in ``settings.py``
e.g.::

    INSTALLED_APPS = (
        "countries",
        "postal",
        ...
        )

3. Add a ``postal_form`` to your templates::

    some_template.html
    {% load postal_tags %}
    <html>
        <head>
            <script src="{{ MEDIA_URL }}js/jquery-1.4.2.min.js" type="text/javascript" charset="utf-8"></script>
        </head>
    <body>
        <form method="POST" action="">
            {% csrf_token %}
            {{form.as_p}}
            {% monitor_country_change %}
            <script type="text/javascript">
                $('form').monitor_country_change('#id_country');
            </script>
            <input type="submit"/>
        </form>
    </body>
    </html>

Changing the country in the form above should localise the address form.

3. In your view code add code to save the addressform e.g.::

    from postal.forms import PostalAddressForm

    def my_view(request)
    	if request.method == "POST":
            address_form = PostalAddressForm(request.POST, prefix=request.POST.get('prefix', ''))
            address_form.save()


How to use localised addresses
==============================

Address localisation is turned on by default. To turn off Address l10n in ``settings.py`` set::

	POSTAL_ADDRESS_L10N = False


Customize address labels and requirement
----------------------------------------

If you wish to customize the address labels and whether the address line is
required or not, you can add the following variables to settings.py::

	POSTAL_ADDRESS_LINE1, POSTAL_ADDRESS_LINE2, POSTAL_ADDRESS_CITY, POSTAL_ADDRESS_STATE, POSTAL_ADDRESS_CODE

Each of these variables is set to a tuple of the format ``('label', True/False)``
``label`` is used to label the field, and the second boolean value sets whether
the field is required or not, e.g.::

	POSTAL_ADDRESS_LINE1 = ("Department", True)

BUILD HISTORY
=============

0.9.6
Remove django-piston requirement
Fixed django 1.7 compatibility issues
Added Italian Postal Address Form
(Thanks to Francesco Facconi for above changes)

0.7.2
Major refactor where all models removed so django-postal just provides localized forms.
It is up to the supporting project to define their own address models

0.4
Don't enforce uniqueness on postal addresses

Developers, How to Contribute
=============================

Git foo::

    $ git clone git@github.com:mthornhill/django-postal.git
    $ cd django-postal
    $ virtualenv . --no-site-packages
    $ source bin/activate
    $ python bootstrap.py
    $ bin/buildout -v
    $ bin/django syncdb
    $ bin/django test postal
    $ bin/django runserver

Browse to http://localhost:8000

New countries can be added to the `src/postal/forms` folder by their
2 letter country code e.g. ``us``

Each country folder contains an ``__init__.py`` and a ``forms.py``

``forms.py`` contains the localized address.

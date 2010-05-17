"""
Model of Postal Address, could possibly use some ideas from
http://www.djangosnippets.org/snippets/912/ in the future
"""
# django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# other imports
from countries.models import Country

class PostalAddress(models.Model):
    # corresponds to a street address or house name
    line1 = models.CharField(_("line1"), max_length=100, default=u'', blank=True, null=True)

    # corresponds to a village, area or locality
    line2 = models.CharField(_("line2"), max_length=100, default=u'', blank=True, null=True)

    # corresponds to a town, or city
    city = models.CharField(_("Town/City"), max_length=100, default=u'', blank=True, null=True)

    # corresponds to state, province  or county
    state = models.CharField(_("State/Province/County"), max_length=100, default=u'', blank=True, null=True)

    # corresponds to zip code or postcode
    code = models.CharField(_("Zip Code/PostCode"), max_length=100, default=u'', blank=True, null=True)

    # country
    country = models.ForeignKey(Country, verbose_name=_("Country"), blank=True, null=True)

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.line1, self.line2, self.city, self.state, self.code, self.country)

    class Meta:
        verbose_name_plural = "Postal Addresses"

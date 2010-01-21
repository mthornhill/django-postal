"""
Model of Postal Address, could possibly use some ideas from
http://www.djangosnippets.org/snippets/912/ in the future
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from countries.models import Country

class PostalAddress(models.Model):
    firstname = models.CharField(_("Firstname"), max_length=50)
    lastname = models.CharField(_("Lastname"), max_length=50)
    line1 = models.CharField(_("Line 1"), max_length=100, blank=True, null=True)
    line2 = models.CharField(_("Line 2"), max_length=100, blank=True, null=True)
    line3 = models.CharField(_("Line 3"), max_length=100, blank=True, null=True)
    line4 = models.CharField(_("Line 4"), max_length=100, blank=True, null=True)
    line5 = models.CharField(_("Line 5"), max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=_("Country"))

    def __unicode__(self):
        return "%s / %s" % (self.line1, self.line2, self.country)


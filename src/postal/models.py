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
    line1 = models.CharField(_("Line 1"), max_length=100, blank=True, null=True)
    line2 = models.CharField(_("Line 2"), max_length=100, blank=True, null=True)
    line3 = models.CharField(_("Line 3"), max_length=100, blank=True, null=True)
    line4 = models.CharField(_("Line 4"), max_length=100, blank=True, null=True)
    line5 = models.CharField(_("Line 5"), max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, verbose_name=_("Country"), blank=True, null=True)

    def __unicode__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.line1, self.line2, self.line3, self.line4, self.line5, self.country)


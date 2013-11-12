from django import models
from django_countries import CountryField


class BasePostalAddress(models.Model):
    line1 = models.CharField(max_length=100, blank=True)
    line2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)
    country = CountryField()

    class Meta:
        abstract = True

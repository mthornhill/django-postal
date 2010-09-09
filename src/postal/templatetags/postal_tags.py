from django.conf import settings
from django import template
from django.template import RequestContext

from postal.views import address_inline
from postal.library import get_postal_form_class

register = template.Library()


@register.inclusion_tag('postal/address_inline.html')
def show_postal_address(request, prefix="", country_code=None, template_name="postal/address_inline.html"):
    address_form_class = get_postal_form_class(country_code)
    address_form = address_form_class(prefix=prefix)
    return {'address_form': address_form, 'MEDIA_URL': settings.MEDIA_URL, 'prefix': prefix}

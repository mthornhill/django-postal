from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson

from postal.library import get_postal_form_class

def address_inline(request, prefix="", country_code=None, template_name="postal/address_inline.html"):
    """displays postal address with localized fields
    """
    country_prefix = "country"
    prefix = request.POST.get('prefix', prefix)
    if prefix:
        country_prefix = prefix + '-country'
    country_code = request.POST.get(country_prefix, country_code)
    address_form_class = get_postal_form_class(country_code)
    
    if request.method == "POST":    
        address_form = address_form_class(prefix=prefix, data={country_prefix: country_code},)
    else:
        address_form = address_form_class(prefix=prefix)
        
    html = render_to_string(template_name, RequestContext(request, {
        "address_form": address_form,
        "prefix": prefix,
    }))
    
    return html 


def changed_country(request):
    result = simplejson.dumps({
        "postal_address" : address_inline(request),
    })
    return HttpResponse(result)
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils import simplejson

from postal.library import form_factory

def address_inline(request, prefix="", country_code=None, template_name="postal/form.html"):
    """ Displays postal address with localized fields """
    
    country_prefix = "country"
    prefix = request.POST.get('prefix', prefix)
    
    if prefix:
        country_prefix = prefix + '-country'
    
    country_code = request.POST.get(country_prefix, country_code)
    form_class = form_factory(country_code=country_code)
    
    if request.method == "POST":
        data = {}
        for (key, val) in request.POST.items():
            if val is not None and len(val) > 0:
                data[key] = val
        data.update({country_prefix: country_code})
        
        form = form_class(prefix=prefix, initial=data)
    else:
        form = form_class(prefix=prefix)
        
    return render_to_string(template_name, RequestContext(request, {
        "form": form,
        "prefix": prefix,
    }))


def changed_country(request):
    result = simplejson.dumps({
        "postal_address": address_inline(request),
    })
    return HttpResponse(result)
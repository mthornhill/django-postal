from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.library import country_map
from postal.views import get_postal_form_class

def test_postal(request, country_code="ie"):
    country_code = request.GET.get('country_code', country_code)
    countries = []
    for k,v in country_map.items():
        countries.append(k)
    form_class = get_postal_form_class(country_code)
    form = form_class()
        
    context = RequestContext(request, locals())    
    return render_to_response('postal/test.html', context)
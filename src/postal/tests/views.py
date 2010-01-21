from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.library import country_map

def test_postal(request, country_code="ie"):
    form_class = get_postal_form_class(country_code)
    form = form_class()
        
    context = RequestContext(request, locals())    
    return render_to_response('postal/test.html', context)
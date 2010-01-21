from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import PostalAddressForm
from library import country_map

def test_postal(request, country_code="ie"):
    form_class = country_map.get(country_code, PostalAddressForm)
    form = form_class()
        
    context = RequestContext(request, locals())    
    return render_to_response('postal/test.html', context)
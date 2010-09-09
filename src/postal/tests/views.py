from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.library import country_map
from postal.forms import PostalAddressForm

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

def test_postal(request):
    countries = []
    for k,v in country_map.items():
        countries.append(k)
    
    result = ""
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            for k,v in form.cleaned_data.items():
                result = result + k + " -> " + v + "<br/>"
                
            address_form = PostalAddressForm(request.POST, prefix=request.POST.get('prefix', ''))
            if address_form.is_valid():
                for k,v in address_form.cleaned_data.items():
                    result = result + k + " -> " + v + "<br/>"
    else:
        form = MyForm() # An unbound form
        
    context = RequestContext(request, locals())    
    return render_to_response('postal/test.html', context)
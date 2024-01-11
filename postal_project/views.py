from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from postal.library import country_map
from postal.forms import PostalAddressForm


def test_postal(request):
    countries = []
    for k, v in country_map.items():
        countries.append(k)

    result = ""
    if request.method == "POST":
        form = PostalAddressForm(request.POST, prefix=request.POST.get("prefix", ""))
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                result = result + k + " -> " + v + "<br/>"
        context = RequestContext(request, locals())
        return render_to_response("postal/test.html", context)
    else:
        form = PostalAddressForm()  # An unbound form

    context = RequestContext(request, locals())
    return render_to_response("postal/test.html", context)


def test_postal_json(request):
    countries = []
    for k, v in country_map.items():
        countries.append(k)

    result = ""
    if request.method == "POST":
        form = PostalAddressForm(request.POST, prefix=request.POST.get("prefix", ""))
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                result = result + k + " -> " + v + "<br/>"
        context = RequestContext(request, locals())
        return render_to_response("postal/test.html", context)
    else:
        form = PostalAddressForm()  # An unbound form

    context = RequestContext(request, locals())
    return render_to_response("postal/test_json.html", context)

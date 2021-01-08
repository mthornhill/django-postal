from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('postal/monitor_country_change.html')
def monitor_country_change():
    return {
        'postal_url': reverse('changed_country'),
    }

from piston.handler import BaseHandler
from postal.library import form_factory

class PostalHandler(BaseHandler):
    allowed_methods = ('GET',)      
    def read(self, request):        
        iso_code=request.GET.get('country', '')
        json = {}
        form_class = form_factory(country_code=iso_code)
        form_obj = form_class()
        for k,v in form_obj.fields.items():
            if k not in json.keys():
                json[k] = {}
            json[k]['label'] = unicode(v.label)
            json[k]['widget'] =  v.widget.render(k,"", attrs={'id': 'id_' + k})
        return json
       

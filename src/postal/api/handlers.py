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
            if k == 'country':
                json[k] = '<label for="id_%s">%s</label>: '%(k,unicode(v.label)) + v.widget.render(k,iso_code)
            else:           
                json[k] = '<label for="id_%s">%s</label>: '%(k,unicode(v.label)) + v.widget.render(k,"")
        return json
       

from django.http import HttpResponse
from django.template import Template, RequestContext

from zcms.models import CMSComponent
from zcms.cmstags import renderComponent

def render_to_response(component,  
                       context = {}, context_instance = {}):
    """ Similar to django render_to_response, this take a context, an 
optional request context, a cms context and a component name. It then 
renders and returns an HttpResponse. The component is a component_cid."""
    context_instance.update(context)
    rendered_component = renderComponent(component_cid = component)
    return HttpResponse( Template(rendered_component).render(context_instance) )
                                

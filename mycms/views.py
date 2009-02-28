from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from zcms.models import CMSComponent
from zcms.cmstags import renderComponent

def showTestPage(request):
    rq = RequestContext(request)
    v = Template(renderComponent(component_cid = 'home')).render(rq)
    return HttpResponse(v)

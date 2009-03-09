from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from zcms.models import CMSComponent
from zcms.cmstags import renderComponent
from zcms import CMSContext
def showTestPage(request, lang='en_gb', channel='UK'):
    rq = RequestContext(request)
    cmsContext = CMSContext(language_iso=lang, channel=channel)
    component = renderComponent(cmsContext, component_cid = 'home')
    v = Template(component).render(rq)
    return HttpResponse(v)

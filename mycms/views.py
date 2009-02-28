from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, RequestContext

from zcms.models import CMSComponent
from zcms.processtools import renderComponent

def showTestPage(request):
    rq = RequestContext(request)
    return HttpResponse(renderComponent('home', rq))

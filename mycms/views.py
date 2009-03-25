from django.template import RequestContext
from zcms import CMSContext
from zcms.page import render_to_response

def showTestPage(request):
    return render_to_response('home', 
                             {'testvar':'MY TEST VALUE'}, 
                             context_instance = RequestContext(request))

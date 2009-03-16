from django.template import RequestContext
from zcms import CMSContext
from zcms.page import render_to_response

def showTestPage(request, lang='en_gb', channel='UK'):
    return render_to_response('home', 
                             {'testvar':'MY VAR'}, 
                             context_instance = RequestContext(request))

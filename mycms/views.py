from django.template import RequestContext
from zcms import CMSContext
from zcms.page import render_to_response

def showTestPage(request, lang='en_gb', channel='UK'):
    cmsContext = CMSContext(language_iso=lang, channel=channel)
    return render_to_response('home', cmsContext,
                             {'testvar':'MY VAR'}, 
                             context_instance = RequestContext(request))

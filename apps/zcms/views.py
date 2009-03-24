""" Views that support the work of the CMS. Note that in all of these the
CMS context is pulled out of the session and put into the thread because the context
processor in the application hasn't been called. Need to weedle out whether this can 
be altered - it will no doubt be a problem for other apps. Wrapping in zcms.setContext
helps of course.
"""
import threading
from django.http import HttpResponseRedirect
from django.http import HttpResponse
 
from zcms import CMSContext
from zcms import setCMSContext
from zcms.models import URL, CMSComponent
from zcms.cmstags import renderComponentDirect
from zcms.cmstags import getElementWithContext 

from django.template import Template, RequestContext

def setContext(request):
    """Set the channel/language CMS context into the session. This a means by which
the channel/language can be set. Use the GET arguments as follows::
    
    channel : channel name
    language : language name
    redirect : page to which to redirect (default to /)

Should either language or channel be missing it is pulled from the existing 
context object in the session.

Should invalid arguments be passed this method fails silently. 
"""
    currentContext = request.session['ZCMS_CONTEXT']
    channel = request.GET.get('channel', currentContext.channel.name)
    language = request.GET.get('language', currentContext.language.iso_code)
    redirect = request.GET.get('redirect', '/')
    try:
        context = CMSContext(language_iso = language, channel = channel)
        setCMSContext(request, context)
    except Exception, ex:
        pass

    return HttpResponseRedirect(redirect)
    
def showPage(request, suffix):
    """ Return a processed static page from the CMS. suffix should match the URL 
field in the URLs table."""
    setCMSContext(request)
    try:
        urlObject = URL.objects.get(enabled = True, url = "/%s"%suffix)
        response = renderComponentDirect(getElementWithContext(CMSComponent, 
                                            cid=urlObject.component_name))
    except Exception, ex:
        print ex
        response = ""

    return HttpResponse( Template(response).render(RequestContext(request)) )
    

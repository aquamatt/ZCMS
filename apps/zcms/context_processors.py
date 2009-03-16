import threading
from zcms import CMSContext

def set_cmscontext(request):
    """ Sets a CMSContext object into the thread object for this request.
Context is drawn for the session (key ZCMS_CONTEXT) or, if it is not there,
it is created with language_id = 1 and channel_id = 1.  
"""
    if not request.session.has_key('ZCMS_CONTEXT'):
        request.session['ZCMS_CONTEXT'] = CMSContext(language_id=1, channel_id=1)
    threading.currentThread()._zcms_context = request.session['ZCMS_CONTEXT']
    return {}
import threading
from zcms import CMSContext

class ZCMSMiddleware(object):
    def process_request(self, request):
        """ Sets a CMSContext object into the thread object for this request.
    Context is drawn for the session (key ZCMS_CONTEXT) or, if it is not there,
    it is created with language_id = 1 and channel_id = 1.  
    """
        assert hasattr(request, 'session'), "The ZCMS middleware requires session middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.sessions.middleware.SessionMiddleware'."
        if not request.session.has_key('ZCMS_CONTEXT'):
            request.session['ZCMS_CONTEXT'] = CMSContext(language_id=1, channel_id=1, site=0)
        threading.currentThread()._zcms_context = request.session['ZCMS_CONTEXT']        
        return None

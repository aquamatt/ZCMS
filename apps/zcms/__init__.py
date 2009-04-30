""" Some basic zCMS objects and add the zcmstags to the Django builtins
so that (a) zextends works as anticipated and (b) you don't always have 
the inconvienience of loading the library in every page."""
from zcms.models import Channel
from zcms.models import Language
import threading

class CMSError(Exception): pass

class CMSContext(object):
    """ Defines the channel/language context of an object """
    def __init__(self, language_id=None, language_iso=None, channel_id=None, channel=None, site=0):
        """ Init with either language id or name and channel id or name. Both
language and channel must be specified. """
        _language = None
        _channel = None
        if language_id:
            _language = Language.objects.get(pk = language_id)
        elif language_iso:
            _language = Language.objects.get(iso_code = language_iso)
            
        if channel_id:
            _channel = Channel.objects.get(pk = channel_id)
        elif channel:
            _channel = Channel.objects.get(name = channel)
            
        if (not _language) or (not _channel):
            raise CMSError("Channel AND Language must be specified to define a context. """)
        
        self.channel = _channel
        self.language = _language
        self.site = site
        
    def parentByChannel(self):
        """ Return new context with channel set to parent, if available """
        if not self.channel.parent:
            return None
        c = CMSContext(language_id = self.language.id, 
                       channel_id = self.channel.parent.id, site=self.site)
        return c
    
    def parentByLanguage(self):
        """ Return new context with language set to fallback language, if possible """
        if not self.language.fallback:
            return None
        c = CMSContext(language_id = self.language.fallback.id, 
                       channel_id = self.channel.id, site = self.site)
        return c
        
    def __str__(self):
        return "%s/%s" % (self.channel.name, self.language.iso_code)
            
    
def setCMSContext(request, context = None):
    """ Set the context found in the session into the thread """
    if context:
        request.session['ZCMS_CONTEXT'] = context
    ct = threading.currentThread()
    ct._zcms_context = request.session['ZCMS_CONTEXT']

# cause tags to get registered so are present by default
from django.template import add_to_builtins
add_to_builtins("zcms.templatetags.zcmstags")

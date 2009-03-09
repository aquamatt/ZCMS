""" Some basic zCMS objects """
from zcms.models import Channel
from zcms.models import Language

class CMSError(Exception): pass

class CMSContext(object):
    """ Defines the channel/language context of an object """
    def __init__(self, language_id=None, language_iso=None, channel_id=None, channel=None):
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
        
    def parentByChannel(self):
        """ Return context for parent channel if indeed this does extend another. """
        if not self.channel.parent:
            return None
        c = CMSContext(language_id = self.language.id, 
                       channel_id = self.channel.parent.id)
        return c
        
    def __str__(self):
        return "%s/%s" % (self.channel.name, self.language.iso_code)
            
    


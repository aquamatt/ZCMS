from zcms.models import *

def init_languages():
    languages = Language.objects.all()
    if languages:
        return
    
    languages = [ ('UK English', 'en_gb', None),
                  ('US English', 'en_us', 'en_gb'),
                  ('French', 'fr_fr', 'en_gb')]

    for name, code, fallback in languages:
        if fallback:
            fb = Language.objects.get(iso_code = fallback)
            l = Language(name = name, iso_code = code, fallback = fb)
        else:
            l = Language(name = name, iso_code = code)
        l.save()
        
def init_channels():
    channels = Channel.objects.all()
    if channels:
        return
    
    channels = [ ('UK', None), ('US', 'UK'), ('FRANCE', 'UK'), ('UK-FOO', 'UK') ]
    for chan, parent in channels:
        c = Channel(name = chan)
        if parent:
            parent = Channel.objects.get(name=parent)
            c.parent = parent
        c.save()

def init_data(**kwargs):
    init_languages()
    init_channels()    

from django.db.models import signals    
signals.post_syncdb.connect(init_data)
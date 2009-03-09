from zcms.models import *

def init_languages():
    languages = Language.objects.all()
    if languages:
        return
    
    languages = [ ('UK English', 'en_gb'),
                  ('US English', 'en_us'),
                  ('French', 'fr_fr')]

    for name, code in languages:
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
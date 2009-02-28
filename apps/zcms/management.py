from zcms.models import *

def init_languages():
    languages = Language.objects.all()
    if languages:
        return
    
    languages = [ ('UK English', 'en/gb'),
                  ('US English', 'en/us'),
                  ('French', 'fr/fr')]

    for name, code in languages:
        l = Language(name = name, iso_code = code)
        l.save()
        
def init_channels():
    channels = Channel.objects.all()
    if channels:
        return
    
    channels = [ 'UK', 'US', 'FRANCE', 'UK-SIMPLE' ]
    for chan in channels:
        c = Channel(name = chan)
        c.save()

def init_data(**kwargs):
    init_languages()
    init_channels()    

from django.db.models import signals    
signals.post_syncdb.connect(init_data)
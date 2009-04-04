"""Update from cmscomponent -> cmscomponent + cmscomponent value"""
from zcms.models import *

def doit():
    parentComponents = {}
    components = CMSComponent.objects.all()
    for c in components:
        pc = parentComponents.get(c.cid, c)
        parentComponents[c.cid] = pc
        cv = CMSComponentValue(component = pc,
                               channel = c.channel,
                               value = c.value)
        cv.save()
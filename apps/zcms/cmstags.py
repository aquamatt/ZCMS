from zcms.models import CMSComponent
from zcms.models import CMSToken
import re

PROCESSORS = {}

# matches 
# [% command arg1 arg2 argn %]
# need to split out args subsequently
commandMatcher = re.compile('(\[% *(\w+) +([\w ]*) *%\])')

def renderComponent(component_cid = None, component_id = None):
    if component_id:
        component = CMSComponent.objects.get(pk = component_id)
    elif component_cid:
        component = CMSComponent.objects.get(cid = component_cid)
    else:
        raise Exception("You must specify a name or id for the component")
    
    value = component.value
    
    commands = commandMatcher.findall(value)
    replacementValues = {}
    for cmstag in commands:
        if replacementValues.has_key(cmstag):
            continue
        tag, cmd, args = cmstag
        rv = getHandler(cmd)(args)
        replacementValues[cmstag] = (tag, rv)
        
    for tag, rv in replacementValues.values():
        print("Replacint %s with %s" % (tag, rv))
        value = value.replace(tag, rv)
    
    return value    
    

def register(tag_name, processor):
    """ Register a CMS tag processor method """
    PROCESSORS[tag_name] = processor
    
def getHandler(tag_name):
    """ Return a CMS tag handler """
    return PROCESSORS[tag_name]
    
#### PREBUILT HANDLERS ######    
    
def handle_componentByName(args):
    """ Return processed component as referenced by name (cid)"""
    cid = args.strip().split(' ')[0].strip()
    return renderComponent(component_cid = cid)
    
def handle_componentById(args):
    """ Return processed component as referenced by ID (primary key)"""
    id = args.strip().split(' ')[0].strip()
    return renderComponent(component_id = int(id))

def handle_tokenByName(args):
    """ Return named token """
    cid = args.strip().split(' ')[0].strip()
    return CMSToken.objects.get(cid = cid).value

def handle_tokenById(args):
    """ Return token referenced by ID (primary key) """
    id = args.strip().split(' ')[0].strip()
    return CMSToken.objects.get(pk = id).value

register('componentByName', handle_componentByName)
register('componentById', handle_componentById)
register('tokenByName', handle_tokenByName)
register('tokenById', handle_tokenById)

from zcms.models import CMSComponent
from zcms.models import CMSToken
from zcms import CMSError
from zcms import CMSContext
import threading
import re

PROCESSORS = {}

# matches 
# [% command arg1 arg2 argn %]
# need to split out args subsequently
commandMatcher = re.compile('(\[% *(\w+) +([\w ]*) *%\])')

def getElementWithContext(cls, **kwargs):
    """ Return a component or token,
first looking in the context specified, then looking to parent contexts if the element
cannot be found. Gives component inheritence.

If the cls is a CMSComponent, the parent will be sought by looking up the channel tree;
if a CMSToken it will look for fallback languages. This enforces the concept that
components are structural whilst Tokens are purely linguistic."""
    if cls == CMSComponent:
        parentField = 'channel'
        parentMethod = 'parentByChannel'
    elif cls == CMSToken:
        parentField = 'language'
        parentMethod = 'parentByLanguage'
    else:
        raise Exception("Can only operate on CMSToken or CMSComponent")
        
    context = threading.currentThread()._zcms_context

    while True:
        try:
            kwargs[parentField] = getattr(context, parentField)
            element = cls.objects.get(**kwargs)
            break
        except Exception, ex:
            p = getattr(context, parentMethod)()
            if not p:
                raise CMSError("Component not available for specified context. ")
            else:
                context = p
    return element
        
def renderComponent(component_cid = None, component_id = None):
    """ Render component specified by either CID or ID for the request's CMS Context. """
    if component_id:
        component = getElementWithContext(CMSComponent, pk=component_id)
    elif component_cid:
        component = getElementWithContext(CMSComponent, cid = component_cid)

    else:
        raise Exception("You must specify a name or id for the component")

    return renderComponentDirect(component)
    
def renderComponentDirect(component):
    """ Render the component object supplied. """
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
    token = getElementWithContext(CMSToken, cid = cid)
    return token.value

def handle_tokenById(args):
    """ Return token referenced by ID (primary key) """
    id = args.strip().split(' ')[0].strip()
    token = getElementWithContext(CMSToken, pk = id)
    return token.value

register('componentByName', handle_componentByName)
register('componentById', handle_componentById)
register('tokenByName', handle_tokenByName)
register('tokenById', handle_tokenById)

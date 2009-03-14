from zcms.models import CMSComponent
from zcms.models import CMSToken
from zcms import CMSError
from zcms import CMSContext
import re

PROCESSORS = {}

# matches 
# [% command arg1 arg2 argn %]
# need to split out args subsequently
commandMatcher = re.compile('(\[% *(\w+) +([\w ]*) *%\])')

def _getElementWithContext(cls, context, **kwargs):
    """ Return a component or token (anything that has channel/language varients,
first looking in the context specified, then looking to parent contexts if the element
cannot be found. Gives component inheritence."""
    while True:
        try:
            element = cls.objects.get(channel = context.channel,
                                        language = context.language,
                                        **kwargs)
            break
        except Exception, ex:
            p = context.parentByChannel()
            if not p:
                raise CMSError("Component not available for specified context. ")
            else:
                context = p
    return element
        
def renderComponent(context = None, component_cid = None, component_id = None):
    """ Render component specified by either CID or ID for the given context. """
    if (not context) or (not isinstance(context, CMSContext)):
        raise CMSError("Context not supplied")

    if component_id:
        component = _getElementWithContext(CMSComponent, context, pk=component_id)
    elif component_cid:
        component = _getElementWithContext(CMSComponent, context, cid = component_cid)
            
    else:
        raise Exception("You must specify a name or id for the component")
    
    value = component.value
    
    commands = commandMatcher.findall(value)
    replacementValues = {}
    for cmstag in commands:
        if replacementValues.has_key(cmstag):
            continue
        tag, cmd, args = cmstag
        rv = getHandler(cmd)(context, args)
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
    
def handle_componentByName(context, args):
    """ Return processed component as referenced by name (cid)"""
    cid = args.strip().split(' ')[0].strip()
    return renderComponent(context, component_cid = cid)
    
def handle_componentById(context, args):
    """ Return processed component as referenced by ID (primary key)"""
    id = args.strip().split(' ')[0].strip()
    return renderComponent(context, component_id = int(id))

def handle_tokenByName(context, args):
    """ Return named token """
    cid = args.strip().split(' ')[0].strip()
    token = _getElementWithContext(CMSToken, context, cid = cid)
    return token.value

def handle_tokenById(context, args):
    """ Return token referenced by ID (primary key) """
    id = args.strip().split(' ')[0].strip()
    token = _getElementWithContext(CMSToken, context, pk = id)
    return token.value

register('componentByName', handle_componentByName)
register('componentById', handle_componentById)
register('tokenByName', handle_tokenByName)
register('tokenById', handle_tokenById)

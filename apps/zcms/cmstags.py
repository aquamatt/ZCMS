from zcms.models import CMSComponent
from zcms.models import CMSToken
from zcms.models import Slot
from zcms import CMSError
from zcms import CMSContext
import threading
import re
from cStringIO import StringIO

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

from datetime import datetime
def _datecmp(year, month, day, date):
    """ Return comparison with datetime instance supplied in date. 
-1 if less than, 0 if equal, +1 if greater than. Time component is ignored.

Used by handle_slot
"""
    rv = cmp(year, date.year)
    if not rv:
        rv = cmp(month, date.month)
    if not rv:
        rv = cmp(day, date.day)
    return rv

def _timecmp(h, m, s, time):
    """ Return comparison with datetime instance supplied in time. 
-1 if less than, 0 if equal, +1 if greater than. Date component is ignored.

Used by handle_slot
"""
    rv = cmp(h, time.hour)
    if not rv:
        rv = cmp(m, time.minute)
    if not rv:
        rv = cmp(s, time.second)
    return rv

def chop(s):
    """ Old fave, chop out trailing white space, CR, LF """
    while s and s[-1] in ['\r','\n',' ', chr(0)]:
        s=s[:-1]
    return s

def strip_null(s):
    """ Getting nulls in string from DB? Clean with this method """
    return "".join([c for c in s if ord(c)>0])

def handle_slot(args):
    """ Takes one argument, the slot name and evaluates the slot entries
one by one, returning the first for which all conditions match. 

Evaluation is done with the following globals dict:
    - now (set to datetime.now)
    - datetime (datetime class)
    - datecmp (date comparison - args: year, month, day, datetime instance)
    - timecmp (time comparison - args: hour, minute, second, datetime instance)
    
See models.Slot for details.
"""
    name = args.strip().split(' ')[0].strip()
    
    _globals = {'now' : datetime.now(),
                'datetime' : datetime,
                'datecmp' : _datecmp,
                'timecmp' : _timecmp,
                }
    
    _locals = {}
    slots = Slot.objects.filter(slot=name, enabled=True).order_by('rank')

    for slot in slots:
        rules = chop(slot.rules).strip()
        if not rules:
            # empty rule set
            continue
        rules = StringIO(rules)
        for rule in rules:
            # why are nulls coming back from DB? Who knows - but 
            # we need to strip them for eval to work
            rule = chop(strip_null(rule))
            if (not rule) or rule[0] == '#' :
                continue
#            print("Testing: [%s]" % (rule,))
            v = eval(rule, _globals, _locals)
            if not v:
                # there's a false rule in this set, can't use this slot
                break
        else:
            # all rules true -this is a winner!
            if slot.is_token:
                return getElementWithContext(CMSToken, cid = slot.component).value
            else:
                return renderComponent(component_cid = slot.component)
    else:
        # loop fell through without finding a winning slot entry
        # return blank
        return ""

register('componentByName', handle_componentByName)
register('componentById', handle_componentById)
register('tokenByName', handle_tokenByName)
register('tokenById', handle_tokenById)
register('slot', handle_slot)

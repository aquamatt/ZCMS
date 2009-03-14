""" Helper tags for using Django templates within the zCMS. Solves problems
such as extending templates. The Django 'extends' tag doesn't understand the CMS
so we provide zextends. """

from django.template import Template
from zcms.cmstags import renderComponent

from zcms import CMSContext
def do_zextends(parser, tokens):
    """ Use only {% zextends template-name %}. Retrieves and processes template 
then passes to Django's 'extends' tag processor. """
    
    # this needs to take the name and pass to a ZExtends render class
    # this can pull the Template, add to context and then instantiate
    # original Extends class and return rendering from that.

    # hard code context
    context = CMSContext(language_iso='en_gb', channel_id=1)
    bits = tokens.contents.split()
    component = renderComponent(context, bits[1])
    return do_extends(Template(component))

register = Library()


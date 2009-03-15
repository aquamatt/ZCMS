""" Helper tags for using Django templates within the zCMS. Solves problems
such as extending templates. The Django 'extends' tag doesn't understand the CMS
so we provide zextends. """

from django.template import Template, Node, Library
from django.template.loader_tags import ExtendsNode
from zcms.cmstags import renderComponent
from zcms import CMSContext
register = Library()

class ZextendsNode(Node):
    def __init__(self, nodelist, parent_name_expr, name):
        Node.__init__(self)
        self.nodelist = nodelist
        self.parent_name_expr = parent_name_expr
        self.name = name

    def render(self, context):
        # hard code context !!!
        cmscontext = CMSContext(language_iso='en_gb', channel_id=1)
        component = renderComponent(cmscontext, self.name)
        context['zcms_internal_component_'] = Template(component)
        en = ExtendsNode(self.nodelist, None, self.parent_name_expr)
        return en.render(context)

def do_zextends(parser, tokens):
    """ Use only {% zextends template-name %}. Retrieves and processes template 
then passes to Django's 'extends' tag processor. """

    bits = tokens.contents.split()
    nodelist = parser.parse()
    parent_name_expr = parser.compile_filter('zcms_internal_component_')
    return ZextendsNode(nodelist, parent_name_expr, bits[1])

register.tag("zextends", do_zextends)

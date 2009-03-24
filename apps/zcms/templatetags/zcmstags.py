""" Helper tags for using Django templates within the zCMS. Solves problems
such as extending templates. The Django 'extends' tag doesn't understand the CMS
so we provide zextends. """

from django.template import Template, Node, Library
from django.template.loader_tags import ExtendsNode
from zcms.cmstags import renderComponent
register = Library()

class ZExtendsNode(Node):
    def __init__(self, nodelist, contextNameExpr, templateName = None, templateVar = None):
        Node.__init__(self)
        self.nodelist = nodelist
        self.contextNameExpr = contextNameExpr
        self.templateName = templateName
        self.templateVar = templateVar

    def render(self, context):
        if self.templateVar:
            name = context[self.templateVar]
        else:
            name = self.templateName
        component = renderComponent(name)
        context['zcms_internal_component_'] = Template(component)
        en = ExtendsNode(self.nodelist, None, self.contextNameExpr)
        return en.render(context)

def do_zextends(parser, token):
    """ Use only {% zextends template-name %}. Retrieves and processes template 
then passes to Django's 'extends' tag processor. 

Similar behaviour to built-in extends tag. It tag may be used in two ways: 
``{% zextends "base" %}`` (with quotes)
uses the literal value "base" as the name of the parent template to extend,
or ``{% zextends variable %}`` uses the value of ``variable`` as the
name of the parent template to extend.
"""
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "'%s' takes one argument" % bits[0]
    templateName, templateVar = None, None
    if bits[1][0] in ('"', "'") and bits[1][-1] == bits[1][0]:
        templateName = bits[1][1:-1]
    else:
        templateVar = bits[1]
    # the contextNameExpr is needed by the Django ExtendsNode - haven't looked into
    # making this less hacky - room for improvement!
    contextNameExpr = parser.compile_filter("zcms_internal_component_")
    nodelist = parser.parse()
    if nodelist.get_nodes_by_type(ZExtendsNode):
        raise TemplateSyntaxError, "'%s' cannot appear more than once in the same template" % bits[0]
    return ZExtendsNode(nodelist, contextNameExpr, templateName, templateVar)

register.tag("zextends", do_zextends)



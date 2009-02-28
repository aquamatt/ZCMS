from django import template
from django.template import Node, TemplateSyntaxError
from django.conf import settings
from django.template import Template

from zcms.models import CMSToken, CMSComponent
from zcms.processtools import renderComponent

register = template.Library()

class GetTokenByNameNode(template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        token = CMSToken.objects.get(cid = self.name)
        return unicode(token.value)

def do_get_token_by_name(parser, token):
    """
    {% getTokenByName name %}
    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError, "'%s' tag takes one argument" % bits[0]
    return GetTokenByNameNode(bits[1])

register.tag('getTokenByName', do_get_token_by_name)

class GetComponentByNameNode(template.Node):
    def __init__(self, name):
        self.name = name

    def render(self, context):
        return renderComponent(self.name, context)

def do_get_component_by_name(parser, component):
    """
    {% getComponentByName name %}
    """
    bits = component.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError, "'%s' tag takes one argument" % bits[0]
    return GetComponentByNameNode(bits[1])

register.tag('getComponentByName', do_get_component_by_name)

from django import template
register = template.Library()

#@register.filter
#def markdown(value):
#    return markdown2.markdown(value)
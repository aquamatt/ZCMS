from django.template import Template
from zcms.models import CMSComponent

def renderComponent(component_cid, context):
    component = CMSComponent.objects.get(cid = component_cid)
    control_head = "{% load cmstags %}"
    value = "%s%s" % (control_head, component.value)
    return Template(value).render(context)

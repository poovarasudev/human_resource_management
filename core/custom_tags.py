from django import template
from django.template import Context, Template

from . import constants

register = template.Library()


@register.simple_tag
def get_constant(name):
    return getattr(constants, name)

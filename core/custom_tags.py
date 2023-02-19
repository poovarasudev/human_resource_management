from django import template
from django.urls import resolve
from django.template import Context, Template

from . import constants

register = template.Library()


@register.simple_tag(takes_context=True)
def set_active(context, name):
    current_route_name = resolve(context['request'].path_info).url_name
    if current_route_name == name:
        return "active"
    return ""


@register.simple_tag
def get_constant(name):
    return getattr(constants, name)

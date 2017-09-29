# -*- coding: utf-8 -*-

from django import template

from admin_interface.models import Theme
from admin_interface.version import __version__

register = template.Library()

try:
    assignment_tag = register.assignment_tag
except AttributeError:
    assignment_tag = register.simple_tag


@assignment_tag(takes_context=True)
def get_admin_interface_theme(context):

    theme = None
    request = context.get('request', None)

    if request:
        theme = getattr(request, 'admin_interface_theme', None)

    if not theme:
        theme = Theme.get_active_theme()

    if request:
        request.admin_interface_theme = theme

    return theme


@assignment_tag(takes_context=False)
def get_admin_interface_version():
    return __version__

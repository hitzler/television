# -*- coding: utf-8 -*-

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='twoDigits')
def twoDigits(value):
    value = '%02d' % value
    return mark_safe(value)

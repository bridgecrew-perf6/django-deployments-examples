from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out the "arg" from a string
    """
    return value.replace(arg,'')

from django import template

register = template.Library()

@register.filter
def times(value, arg):
    """Multiply the value by the arg."""
    return value * arg

@register.filter
def add(value, arg):
    return value / arg


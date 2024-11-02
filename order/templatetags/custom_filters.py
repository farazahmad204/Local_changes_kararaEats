from django import template

register = template.Library()

_subtotal=0
items=[]
# _total=0
# one_item_price=0

@register.filter
def subtotal(value, arg):
    global  _subtotal,items
    #print(" after subtotal value is ",_subtotal)
    for item in items:
        _subtotal += item

    return _subtotal

@register.filter
def times(value, arg):
    """Multiply the value by the arg."""
    global items
    one_item_price=value * arg
    items.append(one_item_price)
    #print(items)
    return one_item_price

@register.filter
def add(value, arg):
    return value / arg









from django import template

register = template.Library()


@register.filter()
def values(items, attr_name):
    return [getattr(i, attr_name) for i in items]


@register.filter()
def distinct(items):
    return set(items)


@register.filter()
def types(items):
    return type(items)


@register.filter()
def integer(items):
    return int(items)


@register.filter()
def string(items):
    return str(items)


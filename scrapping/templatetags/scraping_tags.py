from django import template

register = template.Library()

@register.filter(name='split_then_space')
def split_then_space(value, delimeter):
    return ' '.join(value.split(delimeter))

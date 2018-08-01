from django import template

# register filter
register = template.Library()

@register.filter(name='cut')

def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

# pass in as a string the name of filter
# then pass the function itself
# register.filter('cut', cut)

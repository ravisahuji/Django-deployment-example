from django import template

# create an object called register
register = template.Library()


def txt_replace(value,args):
    """ 
    this is cut out all values of 'agrs' from the string
    """

    return value.replace(args,'')

# 1st method to 'register' to the 'filter'
register.filter('text_replace',txt_replace)  # take 2 arguments...1st is name of the "filter", 2nd is function name


# 2nd method to 'register' to the 'filter' by using "decorator" method

@register.filter(name = "upCase")
def upCase(value):
    """ 
    change the string into upper case
    """
    return value.upper()



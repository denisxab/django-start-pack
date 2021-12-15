from django import template
register = template.Library() 
# {% load {{ app_name }} %}


@register.simple_tag()
def tagSum(a,b,c):
    """
    {% tagSum 1 2 3 %}
    """
    return a+b+c
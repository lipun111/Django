from django import template
register = template.Library()


def truncate5(value):
    result = value[0:5]
    return result


def truncate_n(value, n):
    result = value[0:n]
    return result


register.filter('t_n', truncate_n)
register.filter('truncate5', truncate5)
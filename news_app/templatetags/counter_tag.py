from django import template

register = template.Library()


@register.simple_tag
def counting(value, user_id):
    """Counting objects in QuerySet with user_id = user_id"""
    return value.filter(user_id=user_id).count()

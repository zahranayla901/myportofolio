
from django import template
 
register = template.Library()

@register.filter
def split(value, delimiter=","):
    """
    Pecah string jadi list berdasarkan delimiter, lalu buang spasi di
    pinggir tiap item. Dipakai buat mecah field technology.
    """
    if not value:
        return []
    return [item.strip() for item in value.split(delimiter) if item.strip()]
 

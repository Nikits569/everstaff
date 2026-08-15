from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape
import re

register = template.Library()

@register.filter
def accent_split(value):
    if not value:
        return ""
    # сначала экранируем весь текст (защита от XSS)
    escaped = escape(value)
    # затем заменяем **текст** на <span class="accent">текст</span>
    result = re.sub(r'\*\*(.+?)\*\*', r'<span class="accent">\1</span>', escaped)
    return mark_safe(result)
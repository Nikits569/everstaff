from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def field(context, obj, field_name):
    lang = context.get('SITE_LANG', 'uk')
    if lang == 'en':
        return getattr(obj, f'{field_name}_en', '') or getattr(obj, field_name, '')
    return getattr(obj, field_name, '')
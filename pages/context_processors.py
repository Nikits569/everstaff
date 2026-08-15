def site_language(request):
    lang = request.COOKIES.get('site_lang', 'uk')
    if lang not in ('uk', 'en'):
        lang = 'uk'
    return {'SITE_LANG': lang}
# pages/middleware.py
from django.utils import translation


class SyncLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.COOKIES.get('site_lang', 'uk')
        if lang not in ('uk', 'en'):
            lang = 'uk'

        translation.activate(lang)
        request.LANGUAGE_CODE = lang

        response = self.get_response(request)

        translation.deactivate()
        return response
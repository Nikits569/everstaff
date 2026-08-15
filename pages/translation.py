from deep_translator import GoogleTranslator


def translate_uk_to_en(text: str) -> str:
    if not text:
        return ''
    try:
        return GoogleTranslator(source='uk', target='en').translate(text)
    except Exception as e:
        print("Translation error:", e)
        return text
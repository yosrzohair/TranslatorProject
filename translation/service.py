from translate import Translator

class TranslationService:
    _cache = {}  # Class-level cache

    @staticmethod
    def translate_text(text: str, target_language: str) -> dict:
        if (text, target_language) in TranslationService._cache:
            return TranslationService._cache[(text, target_language)]

        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(text)  # Fixed typo

        # Store in cache
        TranslationService._cache[(text, target_language)] = {
            "original_text": text,
            "translated_text": translated_text,
            "target_language": target_language,
        }
        return TranslationService._cache[(text, target_language)]

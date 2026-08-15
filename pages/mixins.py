from django.db import models
from .translation import translate_uk_to_en


class AutoTranslateMixin(models.Model):
    TRANSLATABLE_FIELDS = []

    class Meta:
        abstract = True

    def save(self, *args, force_translate=False, **kwargs):
        for field in self.TRANSLATABLE_FIELDS:
            en_field = f"{field}_en"

            if not hasattr(self, en_field):
                continue

            uk_text = getattr(self, field, "") or ""
            en_text = getattr(self, en_field, "") or ""

            # Принудительный перевод
            if force_translate:
                setattr(self, en_field, translate_uk_to_en(uk_text))

            # Автоперевод только если английское поле пустое
            elif not en_text.strip():
                setattr(self, en_field, translate_uk_to_en(uk_text))

        super().save(*args, **kwargs)
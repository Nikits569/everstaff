from django.apps import apps
from django.core.management.base import BaseCommand
from pages.mixins import AutoTranslateMixin

class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in apps.get_models():
            if issubclass(model, AutoTranslateMixin):
                for obj in model.objects.all():
                    obj.save(force_translate=True)
                self.stdout.write(f'{model.__name__}: готово')
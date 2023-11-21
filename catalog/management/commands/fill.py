from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()

        category_list = [
            {'name': 'Обувь', 'description': 'Большой выбор выбор обуви на любой вкус'},
            {'name': 'Одежда', 'description': 'Одежда для спорта и активного отдыха'},
            {'name': 'Аксессуары', 'description': 'Широкий ассортимент аксессуаров. Все модели выполнены из качественных материалов'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

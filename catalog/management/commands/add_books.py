from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление тестовых данных в базу данных"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Фрукты", description="Свежие"
        )
        category1, _ = Category.objects.get_or_create(
            name="Овощи", description="Только с грядки"
        )

        products = [
            {"name": "Яблоки", "price": "350", "category": category},
            {"name": "Груши", "price": "550", "category": category},
            {"name": "Свёкла", "price": "230", "category": category1},
            {"name": "Тыква", "price": "330", "category": category1},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Продукт "{Product.name}" успешно добавлен')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Продукт "{Product.name}" уже существует')
                )

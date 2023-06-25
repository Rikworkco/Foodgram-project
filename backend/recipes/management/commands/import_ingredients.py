import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        with open(
            f'{settings.BASE_DIR}/data/ingredients.csv',
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            for items in reader:
                Ingredient.objects.get_or_create(
                    name=str(items['name']),
                    measurement_unit=str(items['measurement_unit'])
                )
            print('Данные записаны в БД')

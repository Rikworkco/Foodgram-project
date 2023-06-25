import csv

from django.conf import settings
from django.core.management.base import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    help = 'Загрузка данных из csv файлов'

    def handle(self, *args, **options):
        with open(
            f'{settings.BASE_DIR}/data/tags.csv',
            # f'{settings.STATIC_ROOT}/data/tags.csv',
            'r',
            encoding='utf-8'
        ) as csv_file:
            reader = csv.DictReader(csv_file)
            for items in reader:
                Tag.objects.get_or_create(
                    name=str(items['name']),
                    color=str(items['color']),
                    slug=str(items['slug'])
                )
            print('Данные записаны в БД')

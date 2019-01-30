import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname("../" + __file__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'store.settings'

import django

django.setup()

from django.core.management.base import BaseCommand
from country.models import Country, State, City
from country.countries import countries
from country.states import states
from country.cities import cities


class Command(BaseCommand):
    """Добавление странб штатов и городов в БД"""
    help = 'Add BD countries, states, cities'

    def add_countries(self):
        for country in countries:
            Country.objects.create(
                id=country[0],
                sortname=country[1],
                name=country[2],
                phonecode=country[3])
        print("Все страны добавлены")

    def add_states(self):
        for state in states:
            State.objects.create(id=state[0], name=state[1], country_id=state[2])
        print("Все штаты добавлены")

    def add_cities(self):
        for city in cities[:51]:
            City.objects.create(id=city[0], name=city[1], state_id=city[2])
        print("Все города добавлены")

    def handle(self, *args, **options):
        self.add_countries()
        self.add_states()
        self.add_cities()
        self.stdout.write('Success')

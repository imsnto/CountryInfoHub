from django.core.management.base import BaseCommand, CommandError
import requests
from django.db import transaction
from urllib.parse import urlparse
from django.conf import settings
from tqdm import tqdm

from countries.models import Country, Language, Currency, Continent, Timezone, Capital

class Command(BaseCommand):
    help = 'Fetches and saves country data from an external API'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            type=str,
            default=settings.COUNTRY_API_URL,
            help='country info API url'
        )

    def validate_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def fetch_country_data(self, url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise CommandError(f"Error fetching country data: {e}")

    def parse_country_data(self, data):
        countries = []

        for country in data:
            try:
                country_info = {
                    "common_name": country.get("name",{}).get("common", ""),
                    'official_name': country.get("name", {}).get("official",""),
                    'capitals': country.get("capital", []),
                    'population': country.get("population", 0),
                    'area': country.get('area', 0),
                    'region': country.get('region', ""),
                    'subregion': country.get('subregion', ""),
                    'un_member': country.get('unMember', False),
                    'independent': country.get('independent', False),
                    'cca2': country.get('cca2', ""),
                    'cca3': country.get('cca3', ""),
                    'start_of_week': country.get('startOfWeek', ""),
                    'flag_url': country.get('flags', {}).get('png', ''),
                    'coat_of_arms_url': country.get('coatOfArms', {}).get('png', ''),
                    'currencies': country.get('currencies', {}) ,
                    'timezones': country.get('timezones', []) ,
                    'languages': country.get('languages', {}),
                    'borders': country.get('borders', []),
                    'continents': country.get('continents', []),
                }
                countries.append(country_info)
            except (KeyError, TypeError) as e:
                raise CommandError("Error parsing country data: {e}")
        return countries

    def insert_countries(self, countries):
        for country in tqdm(countries, desc="Processing countries"):
            with transaction.atomic():
                try:
                    languages_data = country.pop('languages', {})
                    continents_data = country.pop('continents', [])
                    currencies_data = country.pop('currencies', {})
                    timezones_data = country.pop('timezones', [])
                    borders_data = country.pop('borders', [])
                    capitals = country.pop('capitals', [])

                    country_obj, created = Country.objects.update_or_create(
                        cca3=country.pop('cca3'),
                        defaults=country
                    )

                    for capital in capitals:
                        capital_obj, _ = Capital.objects.get_or_create(country=country_obj, name=capital)

                    language_objs = [
                        Language.objects.get_or_create(code=code, defaults={'name': name})[0]
                        for code, name in languages_data.items()
                    ]

                    currency_objs = [
                        Currency.objects.get_or_create(code=code, defaults={'name': value['name'], 'symbol': value['symbol']})[0]
                        for code, value in currencies_data.items()
                    ]

                    timezone_objs = [
                        Timezone.objects.get_or_create(name=tz)[0]
                        for tz in timezones_data
                    ]

                    continents_objs = [
                        Continent.objects.get_or_create(name=cont)[0]
                        for cont in continents_data
                    ]

                    country_obj.languages.set(language_objs)
                    country_obj.currencies.set(currency_objs)
                    country_obj.timezones.set(timezone_objs)
                    country_obj.continents.set(continents_objs)

                    if borders_data:
                        border_countries = Country.objects.filter(cca3__in=borders_data)
                        country_obj.borders.set(border_countries)
                except Exception as e:
                    print(f"Error inserting country: {e}", country['common_name'])


    def handle(self, *args, **options):
        url = options['url']
        if not self.validate_url(url):
            raise CommandError(f"Invalid URL: {url}")

        data = self.fetch_country_data(url)
        countries = self.parse_country_data(data)
        self.insert_countries(countries)







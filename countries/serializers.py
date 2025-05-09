from rest_framework import serializers

from countries.models import Country, Language, Currency, Continent, Timezone, Capital


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['code', 'name']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name', 'symbol']

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['name']

class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['name']

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = ['name', 'country']

class BorderCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['cca3']

class CountrySerializer(serializers.ModelSerializer):
    language_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Language.objects.all(), write_only=True, source='languages'
    )
    continent_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Continent.objects.all(), write_only=True, source='continents'
    )
    currency_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Currency.objects.all(), write_only=True, source='currencies'
    )
    timezone_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Timezone.objects.all(), write_only=True, source='timezones'
    )
    border_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Country.objects.all(), write_only=True, source='borders'
    )

    # Read-only nested serializers
    languages = LanguageSerializer(many=True, read_only=True)
    capitals = CapitalSerializer(many=True, read_only=True)
    continents = ContinentSerializer(many=True, read_only=True)
    currencies = CurrencySerializer(many=True, read_only=True)
    timezones = TimezoneSerializer(many=True, read_only=True)
    borders = BorderCountrySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'common_name', 'official_name', 'population', 'area', 'region', 'subregion',
                 'un_member', 'independent', 'cca2', 'cca3', 'start_of_week', 'coat_of_arms_url',
                  'flag_url', 'languages', 'capitals', 'continents', 'currencies', 'timezones','borders',
                  'language_ids', 'currency_ids', 'timezone_ids', 'continent_ids', 'border_ids'

                  ] #
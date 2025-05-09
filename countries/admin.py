from django.contrib import admin

from .models import Language, Timezone, Currency, Country, Continent, Capital

@admin.register(Capital)
class CapitalAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'area', 'population']

@admin.register(Timezone)
class TimezoneAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'symbol']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']

@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ['name']
from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "languages"
        ordering = ['name']

class Currency(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'currencies'
        ordering = ['name']

class Continent(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'continents'
        ordering = ['name']

class Timezone(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'timezones'
        ordering = ['name']

class Capital(models.Model):
    country = models.ForeignKey('Country', on_delete=models.CASCADE, related_name='capitals')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'capitals'
        ordering = ['name']
        unique_together = ('country', 'name')

class Country(models.Model):
    common_name = models.CharField(max_length=100)
    official_name = models.CharField(max_length=150, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    subregion = models.CharField(max_length=50, blank=True, null=True)
    un_member = models.BooleanField(default=True)
    independent = models.BooleanField(default=True)
    cca2 = models.CharField(max_length=2, blank=True, null=True, unique=True)
    cca3 = models.CharField(max_length=3, unique=True)
    start_of_week = models.CharField(max_length=10, blank=True, null=True)
    flag_url = models.URLField(max_length=200, blank=True, null=True)
    coat_of_arms_url = models.URLField(max_length=200, blank=True, null=True)

    languages = models.ManyToManyField(Language, related_name='countries')
    continents = models.ManyToManyField(Continent, related_name='countries')
    timezones = models.ManyToManyField(Timezone, related_name='countries')
    currencies = models.ManyToManyField(Currency, related_name='countries')
    borders = models.ManyToManyField('self', symmetrical=True)

    def __str__(self):
        return self.common_name

    class Meta:
        db_table = "countries"
        ordering = ['common_name']
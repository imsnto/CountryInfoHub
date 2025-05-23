# Generated by Django 5.2.1 on 2025-05-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_alter_country_borders_alter_language_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together={('code', 'name')},
        ),
    ]

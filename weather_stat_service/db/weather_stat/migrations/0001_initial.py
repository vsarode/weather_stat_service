# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def create_months(apps, schema_editor):
        db_alias = schema_editor.connection.alias
        Month = apps.get_model("weather_stat","Month")
        Month.objects.using(db_alias).create(name="JAN")
        Month.objects.using(db_alias).create(name="FEB")
        Month.objects.using(db_alias).create(name="MAR")
        Month.objects.using(db_alias).create(name="APR")
        Month.objects.using(db_alias).create(name="MAY")
        Month.objects.using(db_alias).create(name="JUN")
        Month.objects.using(db_alias).create(name="JUL")
        Month.objects.using(db_alias).create(name="AUG")
        Month.objects.using(db_alias).create(name="SEP")
        Month.objects.using(db_alias).create(name="OCT")
        Month.objects.using(db_alias).create(name="NOV")
        Month.objects.using(db_alias).create(name="DEC")
        return
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=124)),
                ('year', models.CharField(max_length=124)),
                ('factor', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=124, null=True)),
                ('month', models.ForeignKey(to='weather_stat.Month')),
            ],
        ),
        migrations.AddField(
            model_name='weatherinfo',
            name='month_values',
            field=models.ManyToManyField(to='weather_stat.WeatherValue'),
        ),
        migrations.RunPython(create_months),
    ]

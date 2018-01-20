from django.db import models


class Month(models.Model):
    name = models.CharField(max_length=124)


class WeatherValue(models.Model):
    month = models.ForeignKey(Month)
    value = models.CharField(max_length=124, null=True)


class WeatherInfo(models.Model):
    country = models.CharField(max_length=124)
    year = models.CharField(max_length=124)
    factor = models.CharField(max_length=124)
    month_values = models.ManyToManyField(WeatherValue)

    def save(self, *args, **kwargs):
        if not self.pk:
            super(WeatherInfo, self).save(*args, **kwargs)
            weather_info = WeatherInfo.objects.get(id=self.id)

            for month in Month.objects.all():
                month_values = WeatherValue.objects.create(
                    month=month)

                weather_info.month_values.add(month_values)
            weather_info.save()
        else:
            super(WeatherInfo, self).save(*args, **kwargs)

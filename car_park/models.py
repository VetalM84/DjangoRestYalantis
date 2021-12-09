from django.db import models
from django.core.validators import RegexValidator


class Driver(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['id']


class Vehicle(models.Model):
    driver_id = models.ForeignKey('Driver', related_name='driver', on_delete=models.SET_NULL,
                                  null=True, verbose_name="Водитель")
    make = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=50, verbose_name='Модель')
    # format example "AA 1234 OO"
    plate_number = models.CharField(validators=[RegexValidator("[A-ZА-Я]{2}\s[0-9]{4}\s[A-ZА-Я]{2}")],
                                    max_length=10, verbose_name='Гос.номер')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')

    def __str__(self):
        return ' '.join([self.make, self.model, self.plate_number])

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['id']

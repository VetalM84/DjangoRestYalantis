# Generated by Django 4.0 on 2021-12-10 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_park', '0006_alter_driver_created_at_alter_driver_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateField(default=datetime.date(2021, 12, 10), editable=False, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateField(default=datetime.date(2021, 12, 10), editable=False, verbose_name='Обновлен'),
        ),
    ]

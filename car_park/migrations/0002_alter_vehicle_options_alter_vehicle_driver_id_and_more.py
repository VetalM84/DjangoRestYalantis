# Generated by Django 4.0 on 2021-12-09 08:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_park', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['id'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='driver', to='car_park.driver', verbose_name='Водитель'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='plate_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[A-ZА-Я]{2}\\s[0-9]{4}\\s[A-ZА-Я]{2}')], verbose_name='Гос.номер'),
        ),
    ]

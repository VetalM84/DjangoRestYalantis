# Generated by Django 4.0 on 2021-12-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_park', '0002_alter_vehicle_options_alter_vehicle_driver_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Обновлен'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Обновлена'),
        ),
    ]
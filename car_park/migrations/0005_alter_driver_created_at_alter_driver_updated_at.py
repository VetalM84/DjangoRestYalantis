# Generated by Django 4.0 on 2021-12-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_park', '0004_alter_driver_created_at_alter_driver_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateField(default='10/12/2021', null=True, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='updated_at',
            field=models.DateField(default='10/12/2021', null=True, verbose_name='Обновлен'),
        ),
    ]

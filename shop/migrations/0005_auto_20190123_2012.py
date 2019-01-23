# Generated by Django 2.1.5 on 2019-01-23 17:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190119_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 17, 12, 54, 525117, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
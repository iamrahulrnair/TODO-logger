# Generated by Django 3.2 on 2021-05-06 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20210506_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 4, 30, 45, 478446, tzinfo=utc)),
        ),
    ]

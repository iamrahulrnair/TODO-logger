# Generated by Django 3.2 on 2021-05-06 05:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0006_alter_data_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 5, 20, 12, 694964, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='data',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to=settings.AUTH_USER_MODEL),
        ),
    ]

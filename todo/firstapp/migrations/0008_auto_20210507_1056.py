# Generated by Django 3.2 on 2021-05-07 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_auto_20210506_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='list_length',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='data',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

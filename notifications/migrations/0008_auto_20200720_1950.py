# Generated by Django 3.0.8 on 2020-07-20 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20200720_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='select_time',
            field=models.TimeField(default=datetime.datetime(2020, 7, 20, 19, 50, 20, 871016)),
        ),
    ]

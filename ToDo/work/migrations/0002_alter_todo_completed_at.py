# Generated by Django 3.2.8 on 2021-10-16 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 16, 18, 21, 52, 223609), null=True),
        ),
    ]
# Generated by Django 2.1.2 on 2019-02-04 04:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20190128_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 4, 54, 0, 243000, tzinfo=utc)),
        ),
    ]

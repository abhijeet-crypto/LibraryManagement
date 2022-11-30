# Generated by Django 3.1.5 on 2022-11-29 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0007_auto_20221129_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='isbn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='issuedbooks',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 14, 19, 13, 37, 949496)),
        ),
        migrations.AlterField(
            model_name='issuedbooks',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
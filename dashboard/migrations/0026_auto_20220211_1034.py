# Generated by Django 2.2 on 2022-02-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_auto_20220211_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfilesdata',
            name='Voltage5',
            field=models.FloatField(default=0),
        ),
    ]

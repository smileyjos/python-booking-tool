# Generated by Django 2.2 on 2022-02-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20210929_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='csvFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=100, null=True)),
                ('date_info', models.DateTimeField(blank=True, null=True)),
                ('file_url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='csvFilesData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_info', models.DateTimeField(max_length=100, null=True)),
                ('plunger_position', models.FloatField(max_length=100, null=True)),
                ('Velocity', models.FloatField(max_length=100, null=True)),
                ('HeadPressure', models.FloatField(max_length=100, null=True)),
                ('CounterPressure', models.FloatField(max_length=100, null=True)),
                ('Temperature1', models.FloatField(max_length=100, null=True)),
                ('Pressure1', models.FloatField(max_length=100, null=True)),
                ('Pressure2', models.FloatField(null=True)),
                ('Voltage1', models.FloatField(null=True)),
                ('Voltage2', models.FloatField(null=True)),
                ('Voltage3', models.FloatField(null=True)),
                ('Voltage4', models.FloatField(null=True)),
                ('Voltage5', models.FloatField(null=True)),
                ('EffectivePressure', models.FloatField(null=True)),
            ],
        ),
    ]

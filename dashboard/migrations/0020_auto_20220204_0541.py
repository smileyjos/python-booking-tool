# Generated by Django 2.2 on 2022-02-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20220202_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfiles',
            name='date_info',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

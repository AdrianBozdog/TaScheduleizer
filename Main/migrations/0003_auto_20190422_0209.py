# Generated by Django 2.1.7 on 2019-04-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20190422_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='zipCode',
            field=models.IntegerField(),
        ),
    ]

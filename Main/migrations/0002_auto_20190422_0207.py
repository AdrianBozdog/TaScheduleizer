# Generated by Django 2.1.7 on 2019-04-22 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='officeHoursEnd',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='officeHoursStart',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='officeNumber',
            field=models.IntegerField(),
        ),
    ]

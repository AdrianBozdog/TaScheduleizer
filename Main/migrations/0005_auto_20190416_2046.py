# Generated by Django 2.1.7 on 2019-04-17 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20190416_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Main.Course'),
        ),
    ]

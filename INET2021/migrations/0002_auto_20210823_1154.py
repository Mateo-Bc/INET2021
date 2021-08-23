# Generated by Django 3.0 on 2021-08-23 11:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INET2021', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='ac_cap',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='local',
            name='max_cap',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='local',
            name='time',
            field=models.ManyToManyField(blank=True, to='INET2021.Time'),
        ),
    ]

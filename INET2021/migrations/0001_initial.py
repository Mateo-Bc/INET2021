# Generated by Django 3.0 on 2021-08-23 13:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=100)),
                ('last_name', models.CharField(default=None, max_length=100)),
                ('username', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField(auto_created=True)),
                ('date', models.DateField(default=0)),
                ('cant', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('max_cap', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('ac_cap', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('address', models.CharField(default=None, max_length=100)),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='INET2021.Manager')),
                ('time', models.ManyToManyField(blank=True, to='INET2021.Time')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-05 00:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant', models.CharField(max_length=255)),
                ('rent_date', models.DateField(default=datetime.datetime.now)),
                ('delivered_date', models.DateField(null=True)),
                ('rented_months', models.IntegerField(default=24)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.apartment')),
            ],
        ),
    ]

# Generated by Django 3.0.2 on 2020-03-29 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Postcode',
            fields=[
                ('postcode', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Country')),
            ],
            options={
                'unique_together': {('city', 'state', 'country')},
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('street_num', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=30)),
                ('postcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Postcode')),
            ],
            options={
                'unique_together': {('street_num', 'street_name', 'postcode')},
            },
        ),
    ]
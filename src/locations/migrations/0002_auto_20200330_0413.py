# Generated by Django 3.0.2 on 2020-03-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcode',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.0.2 on 2020-03-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20200330_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcode',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]

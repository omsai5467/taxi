# Generated by Django 4.1.1 on 2022-09-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxibooking', '0003_customerinformation_taxibooking_cars_cartype'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='priceperday',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

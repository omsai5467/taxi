# Generated by Django 4.1.1 on 2022-09-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxibooking', '0004_cars_priceperday'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='geartype',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cars',
            name='milage',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='cars',
            name='model',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
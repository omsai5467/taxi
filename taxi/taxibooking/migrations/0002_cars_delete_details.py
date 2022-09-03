# Generated by Django 4.1 on 2022-09-03 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxibooking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameOfCar', models.CharField(blank=True, max_length=255)),
                ('carId', models.CharField(blank=True, max_length=255)),
                ('carImg', models.ImageField(upload_to='static/car/images')),
                ('createdAT', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='details',
        ),
    ]
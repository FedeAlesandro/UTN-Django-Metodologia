# Generated by Django 2.2 on 2020-10-24 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0011_auto_20201023_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaldate',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentals.Reservation'),
        ),
    ]
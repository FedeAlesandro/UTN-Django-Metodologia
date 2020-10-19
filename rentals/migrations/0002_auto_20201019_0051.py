# Generated by Django 2.2 on 2020-10-19 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'City', 'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name': 'Facility', 'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterField(
            model_name='rentaldate',
            name='reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentals.Reservation'),
        ),
    ]

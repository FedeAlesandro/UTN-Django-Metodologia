# Generated by Django 2.2 on 2020-10-23 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0010_auto_20201023_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaldate',
            name='reservation',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentals.Reservation'),
        ),
    ]
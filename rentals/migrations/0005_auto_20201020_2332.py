# Generated by Django 2.2 on 2020-10-20 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20201020_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='facility',
            field=models.ManyToManyField(to='rentals.Facility'),
        ),
    ]

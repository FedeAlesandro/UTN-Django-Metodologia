# Generated by Django 2.2 on 2020-10-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0015_auto_20201025_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]

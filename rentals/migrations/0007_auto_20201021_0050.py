# Generated by Django 2.2 on 2020-10-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_estate_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='estate',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='estate',
            name='zone',
            field=models.CharField(max_length=20),
        ),
    ]

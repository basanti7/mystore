# Generated by Django 4.2.2 on 2023-08-02 19:24

from django.db import migrations, models
import shopdue.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopdue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(null=True, upload_to=shopdue.models.generate_unique_filename),
        ),
        migrations.AlterField(
            model_name='bill',
            name='due',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='paid',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
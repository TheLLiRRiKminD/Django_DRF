# Generated by Django 5.0.2 on 2024-04-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0021_alter_course_price_alter_course_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(default='price_1P0mNsDF5H2Kx4xvwBM9T1YE'),
        ),
        migrations.AlterField(
            model_name='course',
            name='stripe_id',
            field=models.CharField(default='prod_PqTKpi4y1jvPPz'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-04-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0015_alter_course_price_alter_course_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(default='price_1P0kxfDF5H2Kx4xvo45kmq2u'),
        ),
        migrations.AlterField(
            model_name='course',
            name='stripe_id',
            field=models.CharField(default='prod_PqRr3JYZ9Gvy05'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-04-01 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0020_alter_course_price_alter_course_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.CharField(default='price_1P0m93DF5H2Kx4xvoaGeH5FQ'),
        ),
        migrations.AlterField(
            model_name='course',
            name='stripe_id',
            field=models.CharField(default='prod_PqT561fKzRtV2M'),
        ),
    ]
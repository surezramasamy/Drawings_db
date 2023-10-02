# Generated by Django 3.2.18 on 2023-03-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calibration', '0005_instruments_list_location_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixture_list',
            name='Remarks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instruments_list',
            name='Status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Conditionally_accepted', 'Conditionally_accepted'), ('Not_Calibrated', 'Not_calibrated')], max_length=100),
        ),
        migrations.AlterField(
            model_name='template_list',
            name='Remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
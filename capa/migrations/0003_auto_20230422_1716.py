# Generated by Django 3.2.18 on 2023-04-22 11:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('capa', '0002_auto_20230407_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capa',
            name='Action_date',
        ),
        migrations.RemoveField(
            model_name='capa',
            name='CAPA_submission_date',
        ),
        migrations.RemoveField(
            model_name='capa',
            name='Containment_date',
        ),
        migrations.RemoveField(
            model_name='capa',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='capa',
            name='Date_closed',
        ),
        migrations.AddField(
            model_name='capa',
            name='action_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capa',
            name='capa_submission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capa',
            name='containment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='capa',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='capa',
            name='date_closed',
            field=models.DateField(blank=True, null=True),
        ),
    ]
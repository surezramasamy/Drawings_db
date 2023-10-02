# Generated by Django 3.2.18 on 2023-05-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capa', '0004_auto_20230424_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='capa',
            name='New_or_repeated',
            field=models.CharField(blank=True, choices=[('Complaint', 'Complaint'), ('Information', 'Information')], default='New', max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='capa',
            name='Part_No',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='capa',
            name='Issue_reported',
            field=models.TextField(max_length=256),
        ),
    ]

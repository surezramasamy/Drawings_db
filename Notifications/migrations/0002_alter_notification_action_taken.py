# Generated by Django 3.2.18 on 2023-02-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='Action_taken',
            field=models.TextField(blank=True, max_length=256),
        ),
    ]
# Generated by Django 3.2.16 on 2022-11-14 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Check_point1', models.CharField(blank=True, max_length=256, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CheckSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Check_point_1', models.CharField(blank=True, max_length=256, null=True)),
                ('Check_point_2', models.CharField(blank=True, max_length=256, null=True)),
                ('Check_point1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='check_point1', to='Calibration.checkpoint')),
                ('Check_point2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Calibration.checkpoint')),
            ],
        ),
        migrations.CreateModel(
            name='Instruments_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Intrument_Serial_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Range', models.CharField(blank=True, max_length=100, null=True)),
                ('Least_count', models.CharField(blank=True, max_length=100, null=True)),
                ('Make', models.CharField(blank=True, max_length=100, null=True)),
                ('Intrument_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Calibration_Freq', models.IntegerField(blank=True, null=True)),
                ('Calibration_Plan', models.DateField(blank=True, null=True)),
                ('Date_of_Calibration', models.DateField(blank=True, null=True)),
                ('Next_calibration_Due', models.DateField(blank=True, editable=False, null=True)),
                ('Status', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Conditionally_accepted', 'Conditionally_accepted')], max_length=100, null=True)),
                ('Report_No', models.CharField(blank=True, max_length=100, null=True)),
                ('Calibration_report1', models.FileField(blank=True, null=True, upload_to='Calibration/Instruments')),
                ('Calibration_report2', models.FileField(blank=True, null=True, upload_to='Calibration/Instruments')),
                ('FN', models.CharField(blank=True, default='REV-01 14.05.2022', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fixture_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(blank=True, max_length=256, null=True)),
                ('Product_description', models.CharField(blank=True, max_length=100, null=True)),
                ('Sub_Assembly', models.CharField(blank=True, max_length=100, null=True)),
                ('Fixture_or_Template_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Location_used', models.CharField(blank=True, max_length=100, null=True)),
                ('Verification_Freq', models.IntegerField()),
                ('Verification_Plan', models.DateField(blank=True, null=True)),
                ('Verified_on', models.DateField(blank=True, null=True)),
                ('Next_Verification_Due', models.DateField(blank=True, editable=False, null=True)),
                ('Status', models.CharField(blank=True, choices=[('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ('Conditionally_accepted', 'Conditionally_accepted')], max_length=100, null=True)),
                ('Remarks', models.CharField(blank=True, max_length=256, null=True)),
                ('Verification_report1', models.FileField(blank=True, null=True, upload_to='Calibration/Fixture_or_Templates')),
                ('Verification_report2', models.FileField(blank=True, null=True, upload_to='Calibration/Fixture_or_Templates')),
                ('checksheet', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Calibration.checksheet')),
            ],
        ),
    ]

# Generated by Django 3.2.18 on 2023-04-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calibration', '0006_auto_20230324_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history1',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history10',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history2',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history3',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history4',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history5',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history6',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history7',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history8',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Calibration_history9',
            field=models.CharField(blank=True, help_text='Date_of_Calibration=05/05/22 ,Due_date= 04/05/22 Calibrated_by =VIPL,Remarks=ok', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='instruments_list',
            name='Format_No',
            field=models.CharField(default='F/QA/01   Rev 01 dt 20.01.23', editable=False, max_length=100),
        ),
    ]

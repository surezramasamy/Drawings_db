from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import User

class Capa(models.Model):
    date = models.DateField(default=now,null=True,blank=True)
   
    Customer =models.CharField(max_length=256)
    Part_name = models.CharField(max_length=256)
    Part_No = models.CharField(max_length=256,null=True,blank=True)
    Sub_assembly = models.CharField(max_length=256,null=True,blank=True)
    type_choices =(("Complaint", "Complaint"),("Information","Information"))
    Type_of_reporting =models.CharField(max_length=256,choices =type_choices,default ="Information",null=True,blank=True )
    Issue_reported =models.TextField(max_length=256)
    New_or_repeat_choices =(("New", "New"),("Repeated","Repeated"))
    New_or_repeated =models.CharField(max_length=256,choices =New_or_repeat_choices,default ="New",null=True,blank=True ) 
    
    Defect_photo=models.FileField(blank=True,upload_to='capa/Defect',null=True)
    Team_Involved=models.CharField(max_length=256,null=True,blank=True)
    Qty_rejected =models.CharField(max_length=256,null=True,blank=True)
    Containment_details  =models.CharField(max_length=256,null=True,blank=True)
    containment_date = models.DateTimeField(null=True,blank=True)
   
    Reason_or_Root_cause = models.TextField(null=True,blank=True)
    Action = models.TextField(null=True,blank=True) 
    Action_photo=models.FileField(blank=True,upload_to='capa/Action',null=True) 
    action_date = models.DateTimeField(null=True,blank=True)     
    
    Action_report1=models.FileField(blank=True,upload_to='capa/Action',null=True) 
    Action_report2=models.FileField(blank=True,upload_to='capa/Action',null=True)
    Action_report3=models.FileField(blank=True,upload_to='capa/Action',null=True)  
    capa_submission_date=models.DateTimeField(null=True,blank=True)     
      
    Resp = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)    
    status_choices =(("open", "open"),("closed","closed"))
    Status=models.CharField(max_length=256,choices = status_choices,default ="open",null=True,blank=True )
    date_closed = models.DateTimeField(null=True,blank=True)
    
    Process_Resp = models.CharField(max_length=256,null=True,blank=True)     
    Monitoring_action = models.CharField(max_length=256,null=True,blank=True)
    Lesson_learnt = models.TextField(null=True,blank=True)
    Audit_points = models.CharField(max_length=256,null=True,blank=True)
    Remarks = models.CharField(max_length=256,blank=True)
    def get_absolute_url(self):
        return reverse ("capa_detail",kwargs={'pk':self.pk})
from django.db import models
from datetime import datetime,timedelta
import datetime
from dateutil.relativedelta import relativedelta



class History_card(models.Model):

    Format_No = models.CharField(max_length=100,editable=False,default="F/QA/10   Rev 01 dt 20.01.23")
    
    Date = models.DateField(auto_now=True,null=True,blank=True,editable=False)
    Intrument_Serial_No = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Calibrated_on = models.DateField(null=True,blank=True)
    Calibrated_by=models.CharField(max_length=100,blank=True,null=True)
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                 ("Not_Calibrated","Not_calibrated")
                )
    Status = models.CharField(max_length=100,choices = result)
    Remarks=models.CharField(max_length=100,blank=True,null=True) 


class Instruments_List(models.Model):
    Format_No = models.CharField(max_length=100,editable=False,default="F/QA/01   Rev 01 dt 20.01.23")
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                 ("Not_Calibrated","Not_calibrated")
                )
    Description = models.CharField(max_length=100,blank=True,null=True)
    Intrument_Serial_No = models.CharField(max_length=100,blank=True,null=True)
    Range = models.CharField(max_length=100,blank=True,null=True)
    Least_count = models.CharField(max_length=100,blank=True,null=True)
    Make = models.CharField(max_length=100,blank=True,null=True)
    Location_used=models.CharField(max_length=100,blank=True,null=True)
    Calibration_Freq = models.IntegerField(blank=True,null=True)
    Calibration_Plan =models.DateField(null=True,blank=True)
    Date_of_Calibration =models.DateField(null=True,blank=True)
    Next_calibration_Due =models.DateField(editable=False,null=True,blank=True)
    def save(self):
        if self.Date_of_Calibration == None:
            self.Next_calibration_Due=self.Calibration_Plan
            super(Instruments_List, self).save()
        else:           
            from dateutil.relativedelta import relativedelta
            self.Next_calibration_Due=self.Date_of_Calibration + relativedelta(months=self.Calibration_Freq)-relativedelta(days=1)
            super(Instruments_List, self).save()
  
    Status = models.CharField(max_length=100,choices = result)
    Report_No= models.CharField(max_length=100,blank=True,null=True)
    Calibration_report1 =models.FileField(upload_to='Calibration/Instruments',blank=True,null=True)
    Calibration_report2 =models.FileField(upload_to='Calibration/Instruments',blank=True,null=True)
    Remarks = models.CharField(max_length=100,blank=True,null=True)
    History =models.ForeignKey(History_card,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str(f"Format no= F/QA/10 Rev 01 04.04.23") 
    
    
    

  
    


class Fixture_List(models.Model):
    Customer  = models.CharField(max_length=256,blank=True,null=True)
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                ("Not_verified","Not_verified")
                )

    Product_description  = models.CharField(max_length=100,blank=True,null=True)
    Sub_Assembly  = models.CharField(max_length=100,blank=True,null=True)
    Fixture_or_Template_ID = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Location_used = models.CharField(max_length=100,blank=True,null=True)
    Verification_Freq = models.IntegerField()
    Verification_Plan =models.DateField(null=True,blank=True)
    Verified_on =models.DateField(null=True,blank=True)
    Next_Verification_Due =models.DateField(editable=False,null=True,blank=True)
    def save(self):
        if self.Verified_on == None:
            self.Next_Verification_Due=self.Verification_Plan
            super(Fixture_List, self).save()
        else:           
            from dateutil.relativedelta import relativedelta
            self.Next_Verification_Due=self.Verified_on+relativedelta(months= self.Verification_Freq)
            super(Fixture_List, self).save()
       
       

        
    Status = models.CharField(max_length=100,choices = result)
    Remarks =models.TextField(null=True,blank=True)
    Asset_details =models.CharField(max_length=50,null=True,blank=True)
    Verification_report1 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    Verification_report2 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    
    def __str__(self):
        return str(f"Format no= F/QA/08 Rev 01 04.04.23")
    
        
        
class Template_List(models.Model):
    Customer  = models.CharField(max_length=256,blank=True,null=True)
    result=(   ("Accepted","Accepted"),
                ("Rejected","Rejected"),
                ("Conditionally_accepted","Conditionally_accepted"),
                ("Not_verified","Not_verified")
                )

    Product_description  = models.CharField(max_length=100,blank=True,null=True)
    Sub_Assembly  = models.CharField(max_length=100,blank=True,null=True)
    Fixture_or_Template_ID = models.CharField(max_length=100,blank=True,null=True)
    Description = models.CharField(max_length=100,blank=True,null=True)
    Location_used = models.CharField(max_length=100,blank=True,null=True)
    Verification_Freq = models.IntegerField()
    Verification_Plan =models.DateField(null=True,blank=True)
    Verified_on =models.DateField(null=True,blank=True)
    Next_Verification_Due =models.DateField(editable=False,null=True,blank=True)
    def save(self):
        if self.Verified_on == None:
            self.Next_Verification_Due=self.Verification_Plan
            super(Template_List, self).save()
        else:           
            from dateutil.relativedelta import relativedelta
            self.Next_Verification_Due=self.Verified_on+relativedelta(months= self.Verification_Freq)
            super(Template_List, self).save()
       
      

        
    Status = models.CharField(max_length=100,choices = result)
    Remarks =models.TextField(null=True,blank=True)
    Asset_details =models.CharField(max_length=50,null=True,blank=True)
    Verification_report1 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    Verification_report2 =models.FileField(upload_to='Calibration/Fixture_or_Templates',null=True,blank=True)
    

    def __str__(self):
        return str(f"Format no= F/QA/08 Rev 01 04.04.23")

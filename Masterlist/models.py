from django.db import models

class Rev_History(models.Model):
    Document_Description= models.CharField(max_length=256,null=True,blank=True) 
    Rev_No= models.CharField(max_length=256,null=True,blank=True)
    Rev_Date= models.DateField(null=True,blank=True)
    Rev_History = models.CharField(max_length=256,null=True,blank=True)   
    

class Master_Documents(models.Model):
    Department =models.CharField(max_length=256,null=True,blank=True)
    Document_No= models.CharField(max_length=256,null=True,blank=True)
    Rev_Details =models.ForeignKey(Rev_History,on_delete=models.CASCADE,null=True,blank=True)    
    Document_Description= models.CharField(max_length=256,null=True,blank=True) 
    def get_upload_path(instance, filename):
         return '{0}/{1}/{2}' .format('master_documents',instance.Department,instance.Document_Description)    
    Document_File = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    Remarks =models.CharField(max_length=256,null=True,blank=True)
    
    def __str__(self):
        return self.Document_Description
 
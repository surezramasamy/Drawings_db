from django.db import models



class customer(models.Model):
    customer=models.CharField(max_length=256)
    def __str__(self):
        return self.customer

class Model_Name(models.Model):
    model =models.CharField(max_length=256)
    def __str__(self):
            return self.model
    class Meta:
        ordering = ['model']

class Sub_Assembly(models.Model):
    sub_assembly =models.CharField(max_length=256)
    def __str__(self):
        return self.sub_assembly
class Material(models.Model):
    material =models.CharField(max_length=256)
    def __str__(self):
        return self.material

class Drawings_2D(models.Model):
    Customer = models.ForeignKey(customer,on_delete=models.CASCADE,null=True,blank=True)
    Model_Name = models.ManyToManyField(Model_Name,related_name='model_names',through=None,blank=True,null=True)


    def All_parts_model(self):
        return "\n".join([p.model for p in self.Model_Name.all()])
    Sub_Assembly_Name = models.ForeignKey(Sub_Assembly,on_delete=models.CASCADE,null=True,blank=True)
    Child_part = models.CharField(max_length=256,null=True,blank=True)
    def get_upload_path(instance, filename):
        return '{0}/{1}/{2}' .format('drawings',instance.Sub_Assembly_Name,filename)
    Drawing1 = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    Drawing2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Photo1 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Photo2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Process_Instructions = models.CharField(max_length=256,null=True,blank=True,help_text='optional')
    
class Development_Drawings(models.Model):
    Date_Uploaded=models.DateTimeField(auto_now=True,editable=False)
    Customer = models.ForeignKey(customer,on_delete=models.CASCADE,null=True,blank=True)
    Model_Name = models.CharField(max_length=256,null=True,blank=True)   
    Part_Name  = models.CharField(max_length=256,null=True,blank=True)
    def get_upload_path(instance, filename):
        return '{0}/{1}/{2}' .format('dev_drawings',instance.Customer,filename)
    Drawing1 = models.FileField(upload_to=get_upload_path,blank=True,null=True)
    Drawing2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)    
    Photo1 = models.FileField (upload_to=get_upload_path,blank=True,null=True)    
    Fesability_comments   = models.TextField(null=True,blank=True)    
    Inspection_report1 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Inspection_report2 = models.FileField (upload_to=get_upload_path,blank=True,null=True)
    Sample_details=models.CharField(max_length=256,null=True,blank=True) 
    Process_Instructions = models.CharField(max_length=256,null=True,blank=True,help_text='optional')

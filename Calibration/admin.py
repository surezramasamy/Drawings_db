from django.contrib import admin
from . models import Instruments_List,Fixture_List,Template_List,History_card
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from rangefilter.filters import DateRangeFilter

class Resource1(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource1, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v
    class Meta:
        model = Instruments_List
        fields = ('id','Description','Intrument_Serial_No','Range','Least_count','Make','Location_used','Calibration_Freq','Calibration_Plan','Date_of_Calibration','Next_calibration_Due','Status','Report_No','Calibration_report1','Calibration_report2','Remarks')

        export_order = ['id','Description','Intrument_Serial_No','Range','Least_count','Make','Location_used','Calibration_Freq','Calibration_Plan','Date_of_Calibration','Next_calibration_Due','Status','Report_No','Calibration_report1','Remarks']

class Resource2(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource2, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v


    class Meta:
        model = Fixture_List
        fields = ('id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','checksheet','Verification_report1','Verification_report2','Status','Asset_details','Remarks')

        export_order = ['id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Verification_report1','Verification_report2','Status','Remarks']

class Resource3(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource3, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v


    class Meta:
        model = Template_List
        

        fields = ('id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','checksheet','Verification_report1','Verification_report2','Status','Asset_details','Remarks')

        export_order = ['id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Verification_report1','Verification_report2','Status','Remarks']

class Resource4(resources.ModelResource):
    def export_field(self, field, obj):
        v = super(Resource1, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v
    class Meta:
        model = History_card
        fields = ('Date','Intrument_Serial_No','Description','Calibrated_on','Calibrated_by','Status','Remarks')

        export_order = ['Date','Intrument_Serial_No','Description','Calibrated_on','Calibrated_by','Status','Remarks']



class Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource1
    class Meta:
        model = Instruments_List
    list_display = ['id','Description','Intrument_Serial_No','Range','Least_count','Make','Location_used','Calibration_Freq','Calibration_Plan','Date_of_Calibration','Next_calibration_Due','Status','Report_No','Calibration_report1','Calibration_report2','Remarks']

    list_filter = [('Date_of_Calibration',DateRangeFilter),('Next_calibration_Due',DateRangeFilter),'Description','Make','Status','Location_used']
    search_fields =['Intrument_Serial_No','Description','Make','Location_used','Date_of_Calibration','Next_calibration_Due']
    
    

class Admin1(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource2
    class Meta:
        model = Fixture_List
    list_display = ['id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Status','Verification_report1','Verification_report2','Asset_details','Remarks']
    
    list_filter=[('Verified_on',DateRangeFilter),('Next_Verification_Due',DateRangeFilter),'Customer','Product_description','Sub_Assembly','Location_used','Status','Asset_details']
    search_fields =['Customer','Product_description','Sub_Assembly','Location_used','Verified_on','Next_Verification_Due']
   
class Admin2(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource3
    class Meta:
        model = Template_List
    list_display = ['id','Customer','Product_description','Sub_Assembly','Fixture_or_Template_ID','Description','Location_used','Verification_Freq','Verification_Plan','Verified_on','Next_Verification_Due','Status','Verification_report1','Verification_report2','Asset_details','Remarks']
    
    list_filter=[('Verified_on',DateRangeFilter),('Next_Verification_Due',DateRangeFilter),'Customer','Product_description','Sub_Assembly','Location_used','Status','Asset_details']
    search_fields =['Customer','Product_description','Sub_Assembly','Location_used','Verified_on','Next_Verification_Due']

class Admin4(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource4
    class Meta:
        model = History_card
    list_display = ['Date','Intrument_Serial_No','Description','Calibrated_on','Calibrated_by','Status','Remarks']
    
    list_filter=[('Date',DateRangeFilter),'Description','Intrument_Serial_No','Status']
    search_fields =['Intrument_Serial_No','Description','Intrument_Serial_No']


admin.site.register(Instruments_List,Admin)
admin.site.register(Fixture_List,Admin1)
admin.site.register(Template_List,Admin2)
admin.site.register(History_card,Admin4)


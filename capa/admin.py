from django.contrib import admin
from . models import Capa
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
        model = Capa
        fields = ('date','Customer','Part_name','Part_No','Sub_assembly','Type_of_reporting','Issue_reported','New_or_repeated','Defect_photo','Containment_details','Qty_rejected','containment_date','action_date','capa_submission_date','Status','date_closed','Action','Monitoring_action','Lesson_learnt','Audit_points','Remarks')

        export_order = ['date','Customer','Part_name','Part_No','Sub_assembly','Type_of_reporting','Issue_reported','New_or_repeated','Qty_rejected','containment_date','Containment_details','action_date','capa_submission_date','Status','date_closed','Action','Monitoring_action','Lesson_learnt','Audit_points','Remarks']

   
class Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource1
    class Meta:
        model = Capa
    list_display = ['date','Customer','Part_name','Part_No','Sub_assembly','Type_of_reporting','Issue_reported','New_or_repeated','Defect_photo','Containment_details','Qty_rejected','containment_date','action_date','capa_submission_date','Status','date_closed','Action','Monitoring_action','Lesson_learnt','Audit_points','Remarks']
    list_editable = ['Customer','Part_name','Part_No','Sub_assembly','Defect_photo','Containment_details','Qty_rejected','containment_date','Action','Monitoring_action','Lesson_learnt','Audit_points','Remarks']
    list_filter = [('date',DateRangeFilter),'Customer','Type_of_reporting','New_or_repeated','Part_name','Status']
    

 

admin.site.register(Capa,Admin)

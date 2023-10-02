from django.contrib import admin
from . models import Rev_History,Master_Documents
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE




class Resource(resources.ModelResource):
    # Cleaning of Error During dowload in Xlsx
    def export_field(self, field, obj):
        v = super(Resource, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v
    # Use to convert ForeignKey ID no to Actual vlaue.
    
    Rev_Details = fields.Field(column_name='Rev_Details',attribute = 'Rev_Details',widget=ForeignKeyWidget(Rev_History, 'Rev_History'))

    

    class Meta:
        model = Master_Documents
        export_order = ('Department','Document_No','Rev_Details','Document_Description','Document_File','Remarks')


class Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource
    class Meta:
        model = Master_Documents
  
   
    
    
    

    

admin.site.register(Master_Documents,Admin)
admin.site.register(Rev_History)



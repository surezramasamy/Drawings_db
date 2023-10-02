from django.contrib import admin
from . models import Model_Name,Sub_Assembly,Drawings_2D,customer,Development_Drawings 
from import_export import fields,resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE



'''Drawings_2D'''

from import_export.widgets import ManyToManyWidget

class Resource(resources.ModelResource):
    # Cleaning of Error During dowload in Xlsx
    def export_field(self, field, obj):
        v = super(Resource, self).export_field(field, obj)
        if type(v) == str:
            v = ILLEGAL_CHARACTERS_RE.sub('', v)
        return v
    # Use to convert ForeignKey ID no to Actual vlaue.
    Model_Name = fields.Field(attribute = 'Model_Name',widget=ManyToManyWidget('Model_Name'))
    Sub_Assembly_Name = fields.Field(column_name='Sub_Assembly_Name',attribute = 'Sub_Assembly_Name',widget=ForeignKeyWidget(Sub_Assembly, 'sub_assembly'))

    All_parts_model = fields.Field(attribute = 'All_parts_model')

    class Meta:
        model = Drawings_2D
        export_order = ('Customer','All_parts_model','Sub_Assembly_Name','Child_part','Drawing1','Drawing2','Photo1','Photo2','Process_Instructions')


class Admin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource
    class Meta:
        model = Drawings_2D
    list_display = ['Customer','All_parts_model','Sub_Assembly_Name','Child_part','Drawing1','Drawing2','Photo1','Photo2','Process_Instructions']
    list_filter = ['Customer','Model_Name','Sub_Assembly_Name','Child_part']
    search_fields =['Customer','Model_Name__model','Sub_Assembly_Name__sub_assembly','Child_part','Drawing1','Drawing2']
    list_editable= ['Sub_Assembly_Name','Child_part','Drawing1','Drawing2','Process_Instructions']
    
 

    
class Resource1(resources.ModelResource): 


    class Meta:
        model = Development_Drawings
        export_order = ('Date_Uploaded','Customer','Model_Name','Part_Name','Drawing1','Drawing2','Photo1','Fesability_comments','Process_Instructions')


class Admin1(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Resource1
    class Meta:
        model = Development_Drawings
    list_display = ['Date_Uploaded','Customer','Model_Name','Part_Name','Drawing1','Drawing2','Photo1','Fesability_comments','Sample_details','Process_Instructions']
    list_filter = ['Customer','Model_Name',]
    search_fields =['Customer','Model_Name__model']
    

admin.site.register(Drawings_2D,Admin)
admin.site.register(Model_Name)
admin.site.register(Sub_Assembly)
admin.site.register(customer)
admin.site.register(Development_Drawings,Admin1)
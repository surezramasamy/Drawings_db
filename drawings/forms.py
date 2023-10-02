
from django import forms
from .models import Drawings_2D, Sub_Assembly,Development_Drawings

class LoginForm(forms.Form):
    username =forms.CharField(max_length=200)
    password =forms.CharField(max_length=200)

    def clean(self):
        data =self.cleaned_data
        username =data.get('username')
        password=data.get('password')

        return data

# drawings#
class drgform(forms.ModelForm):
    class Meta:
        model = Drawings_2D
        fields = ['Customer','Model_Name', 'Sub_Assembly_Name']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['Sub_Assembly_Name'].queryset = Sub_Assembly.objects.none()

class drguploadform(forms.ModelForm):
    class Meta:
        model = Drawings_2D
        fields = ('Customer','Model_Name','Sub_Assembly_Name','Child_part','Drawing1','Drawing2','Photo1','Photo2','Process_Instructions')
        
# develoment drawings#

class drgform_dev(forms.ModelForm):
    class Meta:
        model = Development_Drawings
        fields = ['Customer']
        
class drguploadform_dev(forms.ModelForm):
    class Meta:
        model = Development_Drawings
        fields = ('Customer','Model_Name','Part_Name','Drawing1','Drawing2','Photo1','Fesability_comments','Process_Instructions')

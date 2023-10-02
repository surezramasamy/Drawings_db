
from django import forms
from .models import Capa


class Capaform(forms.ModelForm):
    class Meta:
        model = Capa
        fields = ['Type_of_reporting','Status']
        
        
class DateInput(forms.DateInput):
    input_type = 'date'
        
class Capasearchform(forms.Form):
    fromDate=forms.DateField(required=False,widget=DateInput)
    toDate=forms.DateField(required=False,widget=DateInput)
   
    
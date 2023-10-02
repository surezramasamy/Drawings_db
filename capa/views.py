from django.shortcuts import render
from .forms import Capaform,Capasearchform
from .models import Capa
from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView,CreateView
from .import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.db.models import Count
from .utils import get_plot


def CapaListView(request):
    capa = None
    search_form = Capaform(request.POST or None)
            
    if request.method == 'POST':
        Type_of_reporting = request.POST.get('Type_of_reporting')
        Status = request.POST.get('Status')
        capa = Capa.objects.filter(Type_of_reporting=Type_of_reporting,Status=Status)

    context = {
        'search_form': search_form,
        'capa': capa,

    }
    return render(request, 'capa.html',  context)
    
def CapaListView2(request):
    capaqs1 = None
    capaqs2 = None
    search_form2 = Capasearchform(request.POST or None)
         
    if request.method == 'POST':
        fromDate = request.POST.get('fromDate',None)
        toDate = request.POST.get('toDate',None)        
        capaqs1=Capa.objects.filter(date__gte=fromDate,date__lte=toDate) 

        
        

    context = {
        'search_form2': search_form2,
        'capaqs1': capaqs1,

    
      

    }
    return render(request, 'capa2.html',  context)


 
    
class CapaCreateView(CreateView):
    fields = ('date','Customer','Part_name','Sub_assembly','Type_of_reporting','Issue_reported','Qty_rejected')
    model =models.Capa
    success_url = ('/capa')

class CapaUpdateView(UpdateView):    
    model =models.Capa
    fields = ('Defect_photo','Team_Involved','Containment_details','containment_date','Reason_or_Root_cause','Action','action_date','capa_submission_date','Status','date_closed') 
    success_url = ('/capa2')
    def get_form(self):
        form = super().get_form()
        form.fields['containment_date'].widget=DateTimePickerInput()
        form.fields['action_date'].widget=DateTimePickerInput()
        form.fields['capa_submission_date'].widget=DateTimePickerInput()
        form.fields['date_closed'].widget=DateTimePickerInput()
        return form
   
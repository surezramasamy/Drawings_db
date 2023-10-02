from django.shortcuts import render
from django.urls import path
from .import views
from .views import CapaListView,CapaCreateView,CapaUpdateView,CapaListView2


urlpatterns = [
   
    path('capa', views.CapaListView, name='capa'),
    path('capa2', views.CapaListView2, name='capa2'),
     
    path('capacreate',views.CapaCreateView.as_view(),name='capacreate'),    
    path('capaupdate/<int:pk>/', CapaUpdateView.as_view(), name='capaupdate'),

]


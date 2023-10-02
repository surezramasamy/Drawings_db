from django.urls import path
from .views import  HomePageView,DrgPageView,drgupload,drg_dev,drgupload_dev
from . import views


urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('drg', DrgPageView.as_view(), name='drg'),      
    path('drg1', views.drg1, name='drg1'),
    path('drgupload/',views.drgupload, name='drgupload'),
    path('drg_dev', views.drg_dev, name='drg_dev'),
    path('drgupload_dev/',views.drgupload_dev, name='drgupload_dev'),
    



]

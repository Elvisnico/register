from django.urls import path 
from .import views 

urlpatterns = [
    path('register/',views.reg,name='register') ,
    path('',views.view,name='view') 
]

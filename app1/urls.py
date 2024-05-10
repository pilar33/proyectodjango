from django.urls import path
from . import views

urlpatterns = [
      path('index/', views.holaMundo),  
       path('salida/', views.adiosMundo),  
]
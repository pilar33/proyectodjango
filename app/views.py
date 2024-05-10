from django.shortcuts import render
from . import views
# Create your views here.
def hola(request):
    return render(request, "index.html")
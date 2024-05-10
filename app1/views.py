from django.shortcuts import render

# Create your views here.

def holaMundo(request):
    return render(request, 'index1.html')

def adiosMundo(request):
    return render(request, 'salida.html')

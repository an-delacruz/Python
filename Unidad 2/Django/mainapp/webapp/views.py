from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    render(request, 'hola.html')
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from personas.models import Persona
def bienvenido(request):
    personas = Persona.objects.order_by('id')
    return render(request,'bienvenido.html',{'personas':personas})


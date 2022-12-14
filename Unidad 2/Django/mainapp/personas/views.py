from django.shortcuts import redirect, render, get_object_or_404
from personas.forms import PersonaForm

from personas.models import Persona

# Create your views here.
def detallePersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    return render(request,'detalle.html',{'persona':persona})


def nuevaPersona(request):
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona=PersonaForm()        
        return render(request,'agregar.html',{'formaPersona':formaPersona})

def editarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST,instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona=PersonaForm(instance=persona)        
        return render(request,'editar.html',{'formaPersona':formaPersona})
    
def eliminarPersona(request,id):
    persona = get_object_or_404(Persona,pk=id)
    persona.delete()
    return redirect('index')
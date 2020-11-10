from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    testimonios = get_list_or_404(Testimonios, estado = True)
    clientes = get_list_or_404(Clientes, estado = True)
    proyectos = get_list_or_404(Proyectos, estado = True)

    if request.method == 'POST':
        nombre = request.POST.get('name')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        Contactos.objects.create(
            nombre=nombre,
            telefono=telefono,
            email= email,
            asunto = asunto,
            mensaje=mensaje
        )
        messages.success(request, 'Se envío el mensaje!')
        return redirect('index')

    context = {
        'testimonios':testimonios,
        'clientes':clientes,
        'proyectos': proyectos
    }

    return render(request, 'index.html', context)
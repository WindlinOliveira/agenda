from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')

def evento(request, titulo_evento):
    try:
        evento = Evento.objects.get(titulo=titulo_evento)
    except Evento.DoesNotExist:
        return HttpResponse("Evento não encontrado!")

    resposta = evento.local

    return HttpResponse('local: {}'.format(resposta))

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
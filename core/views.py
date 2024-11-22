from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PontodeColetaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import PontodeColeta
from django.http import HttpResponse
import json

def index(request):
        

        return render(request, 'index.html')

def mapa(request):
       return render(request, 'mapa.html')

def sac(request):
       return render(request, 'sac.html')

def CadastrodePontos(request):
    if request.method == 'POST':
        form = PontodeColetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PontodeColetaForm()
            messages.success(request, 'Produto Salvo com sucesso.')
           
            return redirect('vitrine')
            
        else:
            #messages.error(request, 'Erro ao salvar o produto')
            return HttpResponse('Os Dados não foram enviados')
    else:
        form = PontodeColetaForm()
    context = {
        'form': form
    }
    return render(request, 'cadastropontos.html', context)

def vitrine(request):
    context = {
        'vitrine': PontodeColeta.objects.all()  # Altere 'local' para 'vitrine'
    }
    return render(request, 'vitrine.html', context)

def pontomapa(request):
    pontos = PontodeColeta.objects.all()
    pontos_data = [
        {
            'titulo': ponto.titulo,
            'local': ponto.local,
            'coordenadaX': float(ponto.coordenadaX),
            'coordenadaY': float(ponto.coordenadaY)
        }
        for ponto in pontos
    ]
    context = {
        'pontos_json': json.dumps(pontos_data)
    }
    return render(request, 'mapa.html', context)


def perfil(request):
     return render(request, 'perfil.html')
    


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()

        if user:
            return HttpResponse('Já existe o usuário com esse CNPJ ou Email')
        
        user = User.objects.create_user(username=username, first_name=first_name, email=email, password=senha)
        user.save()

        return HttpResponse('usuário cadastrado com sucesso')
     

def login(request):
         if request.method == "GET":
            return render(request, 'login.html')
         else:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

         if user: 
            return HttpResponse('Autenticado')
         else:
            return HttpResponse('Email ou senha inválido')
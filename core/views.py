from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PontodeColetaForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from .models import PontodeColeta
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required



def index(request):
        return render(request, 'index.html')

def mapa(request):
       return render(request, 'mapa.html')

def sac(request):
       return render(request, 'sac.html')



  


def vitrine(request):
    context = {
        'vitrine': PontodeColeta.objects.all()  
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

        return render(request, 'login.html')
     

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)  # Registra o login na sessão
            return redirect('perfil')  # Redireciona para a view de perfil
        else:
            return HttpResponse('Email ou senha inválidos')
         

@login_required
def CadastrodePontos(request):
    if request.user.is_authenticated:
        print('autenticado')
    # Do something for authenticated users.
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
   
    else:
        return render(request, 'login.html')
    


@login_required
def perfil(request):
     username = request.user.username
     first_name = request.user.first_name
     return render(request, 'perfil.html',  {'username': username, 'first_name': first_name})


def sair(request):
    logout(request)  # Remove o usuário da sessão
    return redirect('login')  # Redireciona para a página de login
#programar dps essa birosca
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import PontodeColetaForm, LoginForm
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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)  # Certifique-se de que o campo "username" do usuário é o e-mail
            if user is not None:
                login(request, user)
                return redirect('index')  # Redireciona para a página inicial ou painel do usuário
            else:
                messages.error(request, "Credenciais inválidas. Tente novamente.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
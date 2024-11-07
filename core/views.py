from django.shortcuts import render
from .forms import PontodeColetaForm

def index(request):
        return render(request, 'index.html')

def CadastrodePontos(request):
    form = PontodeColetaForm()
    return render(request, 'cadastropontos.html', {'form': form})


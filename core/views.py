from django.shortcuts import render
from .forms import PontodeColetaForm
from .models import PontodeColeta
from django.http import HttpResponse


def index(request):
        return render(request, 'index.html')

def mapa(request):
       return render(request, 'mapa.html')

def CadastrodePontos(request):
    if request.method == 'POST':
        form = PontodeColetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PontodeColetaForm()
            #messages.success(request, 'Produto Salvo com sucesso.')
            return HttpResponse('Dados enviados com sucesso')
            
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



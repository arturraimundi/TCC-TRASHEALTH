from django.shortcuts import render
from .forms import PontodeColetaForm
from .models import PontodeColeta
def index(request):
        return render(request, 'index.html')

def CadastrodePontos(request):
    form = PontodeColetaForm()
    return render(request, 'cadastropontos.html', {'form': form})

def vitrine(request):
      context = {
            'local' : PontodeColeta.objects.all()
      }
      return render(request, 'vitrine.html', context)
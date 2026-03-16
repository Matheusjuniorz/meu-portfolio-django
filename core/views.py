from django.shortcuts import render
from .models import Projeto

def home(request):
    # Puxa todos os projetos do MySQL
    projetos = Projeto.objects.all() 
    return render(request, 'core/index.html', {'projetos': projetos})
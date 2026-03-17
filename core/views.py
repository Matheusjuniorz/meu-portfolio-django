
import csv
from django.http import HttpResponse, JsonResponse
from .models import Contato, Projeto
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem_texto = request.POST.get('mensagem')

        try:
            send_mail(
                f'Novo contato: {nome}',
                mensagem_texto,
                'batistam032@gmail.com',
                ['batistam032@gmail.com'],
                fail_silently=False,
            )
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem_texto)
            messages.success(request, 'Mensagem enviada com sucesso!')
        except Exception:
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem_texto)
            messages.warning(request, 'Mensagem salva, mas houve um erro ao enviar o alerta por e-mail.')

        return redirect('home')

    return render(request, 'core/index.html', {'projetos': projetos})

def exportar_contatos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contatos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Mensagem', 'Data'])

    contatos = Contato.objects.all().values_list('nome', 'email', 'mensagem', 'data_envio')
    for contato in contatos:
        writer.writerow(contato)

    return response
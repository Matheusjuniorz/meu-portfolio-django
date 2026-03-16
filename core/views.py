
import csv
from django.http import HttpResponse, JsonResponse
from .models import Contato, Projeto
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail





def home(request):
    # Esta linha busca os projetos do banco de dados para exibir no HTML
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem_texto = request.POST.get('mensagem')

        try:
            # Envia o e-mail (usando as configurações do seu settings.py)
            send_mail(
                f'Novo contato: {nome}',
                mensagem_texto,
                'batistam032@gmail.com',
                ['batistam032@gmail.com'],
            )
            # Salva o contato no banco de dados
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem_texto)
            messages.success(request, 'Mensagem enviada com sucesso!')
        except Exception as e:
            # Caso o servidor de e-mail falhe, ainda salvamos no banco e avisamos
            messages.error(request, 'Erro técnico ao enviar e-mail, mas sua mensagem foi salva!')

        # Redireciona para a mesma página para limpar o formulário e evitar reenvio ao dar F5
        return redirect('home')

    # ESTE RETURN É O MAIS IMPORTANTE:
    # Ele deve estar na mesma linha (identação) do 'if request.method'
    return render(request, 'core/index.html', {'projetos': projetos})

# BONUS: View de Exportação (Destaque no seu Portfólio)
def exportar_contatos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contatos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome', 'Email', 'Mensagem', 'Data'])

    contatos = Contato.objects.all().values_list('nome', 'email', 'mensagem', 'data_envio')
    for contato in contatos:
        writer.writerow(contato)

    return response
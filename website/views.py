from django.shortcuts import render
#config de email
from django.core.mail import send_mail
from django.http import JsonResponse

def website(request):
    return render(request, 'home.html')




def enviar_email(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        try:
            # Envie o email
            send_mail(
                'Assunto do Email',
                f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}',
                'noreply@oraculopolitico.com',  # Substitua pelo seu email
                ['contato@oraculopolitico.com'],  # Substitua pelo email de destino
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'mensagem': 'Email enviado com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'mensagem': str(e)})
    else:
        return JsonResponse({'status': 'error', 'mensagem': 'Método não permitido'}, status=405)

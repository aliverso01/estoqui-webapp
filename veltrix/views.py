from django.shortcuts import render
from django.views import View  
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from modulos.produto.models import Produto

def Dashboard(request):
    produtos_count = Produto.objects.filter(user=request.user).count()

    return render(request, 'dashboard.html', {'produtos_count': produtos_count})

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy('dashboard')


class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy('dashboard')
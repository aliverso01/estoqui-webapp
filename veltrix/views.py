from django.shortcuts import render
from django.views import View  
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView, PasswordSetView
from django.contrib.auth.mixins import LoginRequiredMixin 


class DashboardView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Dashboard"
        greeting['heading'] = "Veltrix"
        greeting['subheading'] = "Dashboard" 

        return render(request, 'dashboard.html',greeting)

class MyPasswordChangeView( PasswordChangeView):
    success_url = reverse_lazy('dashboard')


class MyPasswordSetView( PasswordSetView):
    success_url = reverse_lazy('dashboard')

class SecretariaView(LoginRequiredMixin,View):
    def get(self, request):
        greeting = {}
        greeting['title'] = "Secretaria"
        greeting['heading'] = "Veltrix" 
        greeting['subheading'] = "Secretaria" 
        return render(request, 'secretaria.html',greeting)
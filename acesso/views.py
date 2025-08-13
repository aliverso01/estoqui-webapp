from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import PerfilForm
from .models import Perfil

class PerfilView(TemplateView):
    template_name = 'perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfilForm'] = PerfilForm(instance=self.request.user.perfil)
        return context

    def post(self, request, *args, **kwargs):
        perfil_instance = request.user.perfil
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_instance)
        if perfil_form.is_valid():
            perfil_form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Erro ao atualizar perfil. Por favor, corrija os erros abaixo.')
            # Retorna o formulário para exibição com os erros
            return self.render_to_response(self.get_context_data(perfilForm=perfil_form))

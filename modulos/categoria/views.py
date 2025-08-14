from django.shortcuts import render, redirect
from .models import Categoria
from django.contrib.auth.models import User
from .forms import CategoriaForm
from django.contrib import messages
# Create your views here.


def lista_categorias(request):
    categorias = Categoria.objects.filter(user=request.user)
    return render(request, 'categorias/lista.html', {'categorias': categorias})

def create_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.user = request.user
            categoria.save()
            messages.success(request, 'Nova categoria adicionada.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/form.html', {'form': form})

def edit_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria atualizada com sucesso.')
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/form.html', {'form': form})

def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso.')
        return redirect('lista_categorias')
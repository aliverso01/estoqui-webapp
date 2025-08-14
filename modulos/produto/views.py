from django.shortcuts import render, redirect
from modulos.produto.models import Produto
from modulos.produto.forms import ProdutoForm
from django.contrib import messages

# Create your views here.
def lista_produtos(request):
    produtos = Produto.objects.filter(user=request.user)
    return render(request, 'produtos/lista.html', {'produtos': produtos})

def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.user = request.user
            produto.save()
            messages.success(request, 'Novo produto adicionado.')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

def edit_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

def delete_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso.')
        return redirect('lista_produtos')

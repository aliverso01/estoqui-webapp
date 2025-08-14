from django.shortcuts import render, redirect
from .models import FichaTecnica, Insumo
from .forms import FichaTecnicaForm, InsumoForm
from django.contrib import messages

# Create your views here.
def lista_fichas_tecnicas(request):
    fichas_tecnicas = FichaTecnica.objects.filter(user=request.user)
    return render(request, 'ficha_tecnica/lista.html', {'fichas_tecnicas': fichas_tecnicas})

def create_ficha_tecnica(request):
    if request.method == 'POST':
        form = FichaTecnicaForm(request.POST)
        if form.is_valid():
            ficha_tecnica = form.save(commit=False)
            ficha_tecnica.user = request.user
            ficha_tecnica.save()
            messages.success(request, 'Nova ficha técnica adicionada.')
            return redirect('lista_fichas_tecnicas')
    else:
        form = FichaTecnicaForm()
    return render(request, 'ficha_tecnica/form.html', {'form': form})

def edit_ficha_tecnica(request, id):
    ficha_tecnica = FichaTecnica.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        form = FichaTecnicaForm(request.POST, instance=ficha_tecnica)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ficha técnica atualizada com sucesso.') 
            return redirect('lista_fichas_tecnicas')
    else:
        form = FichaTecnicaForm(instance=ficha_tecnica)
    return render(request, 'ficha_tecnica/form.html', {'form': form})

def delete_ficha_tecnica(request, id):
    ficha_tecnica = FichaTecnica.objects.get(id=id, user=request.user)
    if request.method == 'POST':
        ficha_tecnica.delete()
        messages.success(request, 'Ficha técnica deletada com sucesso.')
        return redirect('lista_fichas_tecnicas')
    
def add_insumo(request, ficha_id):
    ficha_tecnica = FichaTecnica.objects.get(id=ficha_id, user=request.user)
    insumos = Insumo.objects.filter(ficha_tecnica=ficha_tecnica)

    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            insumo = form.save(commit=False)
            insumo.ficha_tecnica = ficha_tecnica
            insumo.user = request.user
            insumo.save()
            messages.success(request, 'Insumo adicionado com sucesso.')
            #mantém-se na mesma página
            return redirect('add_insumo', ficha_id=ficha_id)
    else:
        form = InsumoForm()
        
    context = {
        'insumos': insumos,
        'ficha_tecnica': ficha_tecnica,
        'form': form
    }
    return render(request, 'ficha_tecnica/add_insumo.html', context)

def edit_insumo(request, ficha_id, insumo_id):
    ficha_tecnica = FichaTecnica.objects.get(id=ficha_id, user=request.user)
    insumo = Insumo.objects.get(id=insumo_id, ficha_tecnica=ficha_tecnica)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Insumo atualizado com sucesso.')
            return redirect('add_insumo', ficha_id=ficha_id)

def delete_insumo(request, ficha_id, insumo_id):
    ficha_tecnica = FichaTecnica.objects.get(id=ficha_id, user=request.user)
    insumo = Insumo.objects.get(id=insumo_id, ficha_tecnica=ficha_tecnica)
    if request.method == 'POST':
        insumo.delete()
        messages.success(request, 'Insumo deletado com sucesso.')
        return redirect('add_insumo', ficha_id=ficha_id)
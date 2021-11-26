from django.shortcuts import render, redirect
from apps.autor.models import Autor
from apps.autor.form import autorForm
# Create your views here.

def index(request):
    autor = Autor.objects.all().order_by('-id')
    context = {'autor' : autor}
    return render(request, 'autor/inicio.html', context)

def autorCreate(request):
    if(request.method == 'POST'):
        form = autorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('autores:index')
    else:
        form = autorForm()
        return render(request, 'autor/formAutor.html', {'form': form})

def autorEdit(request, id_autor):
    autor = Autor.objects.get(pk=id_autor)

    if(request.method == 'GET'):
        form = autorForm(instance = autor)
    else:
        form = autorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()

        return redirect('autores:index')

    return render(request, 'autor/formAutor.html', {'form': form})

def autorEli(request, id_autor):
    autor = Autor.objects.get(pk=id_autor)
    if(request.method == 'POST'):
        autor.delete()
        return redirect('autores:index')

    return render(request, 'autor/autorEli.html', {'autor': autor})


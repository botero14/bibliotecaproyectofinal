from django.shortcuts import render, redirect
from apps.libro.models import Libro
from apps.libro.form import libroForm
# Create your views here.

def index(request):
    libro = Libro.objects.all().order_by('-id')
    context = {'libro' : libro}
    return render(request, 'libro/inicio.html', context)

def libroCreate(request):
    if(request.method == 'POST'):
        form = libroForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('libros:index')
    else:
        form = libroForm()
        return render(request, 'libro/formLibro.html', {'form': form})

def libroEdit(request, id_libro):
    libro = Libro.objects.get(pk=id_libro)

    if(request.method == 'GET'):
        form = libroForm(instance = libro)
    else:
        form = libroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()

        return redirect('libros:index')

    return render(request, 'libro/formLibro.html', {'form': form})

def libroEli(request, id_libro):
    libro = Libro.objects.get(pk=id_libro)
    if(request.method == 'POST'):
        libro.delete()
        return redirect('libros:index')

    return render(request, 'libro/libroEli.html', {'libro': libro})


from django.shortcuts import render, redirect
from apps.ejemplar.models import Ejemplar
from apps.ejemplar.form import ejemplarForm
# Create your views here.

def index(request):
    ejemplar = Ejemplar.objects.all().order_by('-id')
    context = {'ejemplar' : ejemplar}
    return render(request, 'ejemplar/inicio.html', context)

def ejemplarCreate(request):
    if(request.method == 'POST'):
        form = ejemplarForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ejemplares:index')
    else:
        form = ejemplarForm()
        return render(request, 'ejemplar/formEjemplar.html', {'form': form})

def ejemplarEdit(request, id_ejemplar):
    ejemplar = Ejemplar.objects.get(pk=id_ejemplar)

    if(request.method == 'GET'):
        form = ejemplarForm(instance = ejemplar)
    else:
        form = ejemplarForm(request.POST, instance=ejemplar)
        if form.is_valid():
            form.save()

        return redirect('ejemplares:index')

    return render(request, 'ejemplar/formEjemplar.html', {'form': form})

def ejemplarEli(request, id_ejemplar):
    ejemplar = Ejemplar.objects.get(pk=id_ejemplar)
    if(request.method == 'POST'):
        ejemplar.delete()
        return redirect('ejemplares:index')

    return render(request, 'ejemplar/ejemplarEli.html', {'ejemplar': ejemplar})


from django.shortcuts import render, redirect
from apps.usuario.models import Usuario
from apps.usuario.form import usuarioForm
# Create your views here.

def index(request):
    usuario = Usuario.objects.all().order_by('-id')
    context = {'usuario' : usuario}
    return render(request, 'usuario/inicio.html', context)

def usuarioCreate(request):
    if(request.method == 'POST'):
        form = usuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('usuarios:index')
    else:
        form = usuarioForm()
        return render(request, 'usuario/formUsuario.html', {'form': form})

def usuarioEdit(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)

    if(request.method == 'GET'):
        form = usuarioForm(instance = usuario)
    else:
        form = usuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()

        return redirect('usuarios:index')

    return render(request, 'usuario/formUsuario.html', {'form': form})

def usuarioEli(request, id_usuario):
    usuario = Usuario.objects.get(pk=id_usuario)
    if(request.method == 'POST'):
        usuario.delete()
        return redirect('usuarios:index')

    return render(request, 'usuario/usuarioEli.html', {'usuario': usuario})


from django.shortcuts import render, redirect
from .models import Usuario

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "home.html", {"usuarios": usuarios})

def salvar(request):
    variavelnome = request.POST.get('nome')
    Usuario.objects.create(nome=variavelnome)
    usuarios = Usuario.objects.all()
    return render(request, 'home.html', {'usuarios': usuarios})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    return render(request, 'edit.html', {'usuario': usuario})

def update(request, id):
    variavelnome = request.POST.get('nome')
    usuario = Usuario.objects.get(id=id)
    usuario.nome = variavelnome
    usuario.save()
    return redirect(home)

def delete(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect(home)
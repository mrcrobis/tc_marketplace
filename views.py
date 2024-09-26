from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Produto
from .forms import ProdutoForm

def cadastro_usuario(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('home')

def criar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.vendedor = request.user  # Associa o produto ao vendedor
            produto.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})
